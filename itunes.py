

from collections import OrderedDict

from appscript import app, reference


class Track(object):
    def __init__(self, track):
        self._track = track

    def __repr__(self):
        return u'<Track: {} by {} on {}>'.format(self.name, self.artist,
                                                 self.album)

    @property
    def id(self):
        # return int(self._track.database_ID())
        return int(self._track.id())

    @property
    def name(self):
        return unicode(self._track.name())

    @property
    def artist(self):
        return unicode(self._track.artist())

    @property
    def album(self):
        return unicode(self._track.album())

    @property
    def seconds(self):
        mm, ss = self._track.time().split(':')
        return int(mm) * 60 + int(ss)

    @property
    def year(self):
        return unicode(self._track.year())

    #TODO sort fields

    def play(self):
        return self._track.play()

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.name,
            'artist': self.artist,
            'album': self.album,
            # 'time': self.seconds,
            'year': self.year,
        }


class Playlist(object):
    def __init__(self, playlist):
        self._playlist = playlist
        self._tracks = None

    def __repr__(self):
        return u'<Playlist: {}>'.format(self.name)

    @property
    def name(self):
        return self._playlist.name()

    def _prime_tracks(self):
        if not self._tracks:
            self._tracks = OrderedDict()

            for track in self._playlist.tracks():
                t = Track(track)
                self._tracks[t.id] = t

    @property
    def tracks(self):
        self._prime_tracks()
        return self._tracks.values()

    def get_track(self, id):
        self._prime_tracks()
        return self._tracks.get(id)

    def search(self, query):
        return [Track(track) for track in self._playlist.search(for_=query)]


class Source(object):
    def __init__(self, source):
        self._source = source

    def __repr__(self):
        return u'<Source: {}>'.format(self.name)

    @property
    def name(self):
        return self._source.name()

    @property
    def playlists(self):
        return [Playlist(playlist) for playlist in self._source.playlists()]

    def get_playlist(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist


class iTunes(object):

    def __init__(self):
        self._app = app('iTunes')

        if not self._app.isrunning:
            self._app.run()

    @property
    def sources(self):
        return [Source(source) for source in self._app.sources()]

    def get_source(self, name):
        for source in self.sources:
            if source.name == name:
                return source

    def get_playlist(self, playlist, source=None):
        if source is None:
            source = self.sources[0]
        else:
            source = self.get_source(source)

        return source.get_playlist(playlist)

    @property
    def library(self):
        return self.get_playlist('Music')

    @property
    def current_playlist(self):
        try:
            return Playlist(self._app.current_playlist())
        except reference.CommandError:
            return None

    def play(self, track_id):
        track = self.library.get_track(track_id)
        self._app.current_playlist.play(track._track, once=False)

    def pause(self):
        self._app.pause()

    def stop(self):
        self._app.stop()

    def next(self):
        self._app.next_track()

    def previous(self):
        self._app.back_track()
