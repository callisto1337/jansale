'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('scss', function () {
  return gulp.src('./app/static/scss/style.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./app/static/css/'));
});

gulp.task('default', ['scss'], function () {
  gulp.watch('./app/static/scss/**/*.scss', ['scss']);
});