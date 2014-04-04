/*globals define */
/*jslint nomen: true*/

define([
    'backbone',
    'views/Track',
], function(Backbone, Track) {
    'use strict';

    return Backbone.View.extend({
        el: 'table',

        render: function() {
            this.collection.each(function(track) {
                var trackView = new Track({model: track});
                this.$el.find('tbody').append(trackView.render().$el);
            }, this);

            return this;
        },
    });

});
