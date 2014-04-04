

from flask import (Flask, render_template, make_response, json,
                   send_from_directory, request, abort)

from itunes import iTunes

app = Flask(__name__)
itunes = iTunes()
playlist = itunes.get_playlist('Internet Songs')


def make_json_response(data):
    if not isinstance(data, str):
        data = json.dumps(data)

    resp = make_response(data)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tracks')
def tracks():
    tracks = [track.as_dict() for track in playlist.tracks[:20]]
    return make_json_response(tracks)


@app.route('/tracks/<int:track_id>', methods=['GET', 'POST'])
def track(track_id):
    track = playlist.get_track(track_id)
    if not track:
        abort(404)

    if request.method == 'GET':
        return make_json_response(track.as_dict())

    if request.method == 'POST':
        obj = request.get_json()

        if obj.get('action') == 'play':
            #TODO change to itunes.play(track) if possible
            track.play()
            return ''
        elif obj.get('action') == 'pause':
            itunes.pause()
            return ''
        elif obj.get('action') == 'stop':
            itunes.stop()
            return ''

    abort(400)


@app.route('/static/<path:filename>')
def files(filename):
        return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
