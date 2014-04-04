/*globals define */
/*jslint nomen: true*/

define([
    'models/TrackCollection',
    'views/Playlist',
], function(TrackCollection, Playlist) {
    'use strict';

    new TrackCollection().fetch({
        success: function(collection) {
            new Playlist({collection: collection}).render();
        },
    });
});
