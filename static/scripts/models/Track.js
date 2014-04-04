/*globals define */
/*jslint nomen: true*/

define([
    'backbone',
], function(Backbone) {
    'use strict';

    return Backbone.Model.extend({
        action: function(action) {
            Backbone.$.ajax({
                url: this.url(),
                type: 'POST',
                cache: false,
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify({action: action}),
            });

            this.trigger(action);
        },

        play: function() {
            this.action('play');
        },

        pause: function() {
            this.action('pause');
        },
    });
});
