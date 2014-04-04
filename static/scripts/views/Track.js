/*globals define */
/*jslint nomen: true*/

define([
    'backbone',
], function(Backbone) {
    'use strict';

    return Backbone.View.extend({
        tagName: 'tr',
        className: 'track',

        events: {
            'dblclick': 'togglePlay',
        },

        initialize: function() {
            this.model.view = this;
            this.isPlaying = false;
        },

        delegateEvents: function() {
            Backbone.View.prototype.delegateEvents.apply(this, arguments);

            // this.listenTo(this.model, 'play', this.play);
        },

        togglePlay: function() {
            if (this.isPlaying) {
                this.model.pause();
            } else {
                this.model.play();
            }

            this.isPlaying = !this.isPlaying;
        },

        render: function() {
            this.$el.append('<td></td>');
            this.$el.append('<td>' + this.model.get('title') + '</td>');
            this.$el.append('<td>' + this.model.get('artist') + '</td>');
            this.$el.append('<td>' + this.model.get('album') + '</td>');

            return this;
        },

    });
});
