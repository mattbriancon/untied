

var require = {
    baseUrl: '../static/',

    map: {
        '*': {
            'jquery': 'private-jquery',
            'backbone': 'private-backbone',
            'underscore': 'private-underscore',
        },

        'private-jquery': {'jquery': 'jquery'},
        'private-backbone': {'backbone': 'backbone'},
        'private-underscore': {'underscore': 'underscore'}
    },

    paths: {
        app: 'scripts/app',

        backbone: 'lib/backbone/backbone',
        jquery: 'lib/jquery/dist/jquery.min',
        localstorage: 'lib/backbone.localstorage/backbone.localStorage-min',
        underscore: 'lib/underscore/underscore',

        'private-backbone': 'scripts/private-backbone',
        'private-jquery': 'scripts/private-jquery',
        'private-underscore': 'scripts/private-underscore',

        'constants': 'scripts/Constants',

        'models/Track': 'scripts/models/Track',
        'models/TrackCollection': 'scripts/models/TrackCollection',

        'views/Track': 'scripts/views/Track',
        'views/Playlist': 'scripts/views/Playlist',
    }
};
