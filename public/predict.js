function predict() {
    var canvas = document.getElementById('canvas');
    var image = canvas.toDataURL();
    var imageTensor = tf.fromPixels(canvas);
}