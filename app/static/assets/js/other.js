var img = document.querySelector('.img');
var fullScreen = document.querySelector('.fullscreen');
var close = document.querySelector('.close');
var zoomedImg = document.querySelector('.fullscreen img');

img.addEventListener('click', function() {
    fullScreen.style.display = 'flex';
});

close.addEventListener('click', function() {
    fullScreen.style.display = 'none';
});

zoomedImg.addEventListener('click', function() {
    fullScreen.style.display = 'none';
});
