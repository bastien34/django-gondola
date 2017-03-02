var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');

gulp.task('less', function () {
  return gulp.src('gondola/static/gondola/styles/less/*.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .on('error', onError)
    .pipe(gulp.dest('gondola/static/gondola/styles/css'));
});

gulp.task('default', function () {
   gulp.watch('gondola/static/gondola/styles/less/**/*.less', ['less']);
});

function onError(err){
    console.log(err);
    this.emit('end');
}