module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            dist: {
                src: [
                    'dashboard/static/dashboard/js/dashboard.js'
                ],

                dest: 'dashboard/static/dashboard/dist/js/production.js'
            }
        },

        uglify: {
            build: {
                src: 'dashboard/static/dashboard/dist/js/production.js',
                dest: 'dashboard/static/dashboard/dist/js/production.min.js'
            }
        },

        autoprefixer: {
            options: {
                browsers: ['last 2 versions']
            },
            dist: {
                files: {
                    'dashboard/static/dashboard/dist/css/global.min.css': 'dashboard/static/dashboard/dist/css/global.css'
                }
            }
        },

        watch: {
            options: {
                livereload: false
            },
            scripts: {
                files: ['dashboard/static/dashboard/js/*.js', 'common_components/static/common_components/lib/*.js'],
                tasks: ['concat', 'uglify'],
            },

            css: {
                files: ['dashboard/static/dashboard/sass/*.scss'],
                tasks: ['sass', 'autoprefixer'],
            },
        },

        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: {
                    'dashboard/static/dashboard/dist/css/global.css': 'dashboard/static/dashboard/sass/global.scss'
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-autoprefixer');

    grunt.registerTask('default', ['watch']);
};
