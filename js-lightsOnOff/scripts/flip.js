// Run this function on the loading of the window (DOM highlevel)
window.onload = function() {
    document.getElementById('2').addEventListener('click', function(f) {
        let img = document.getElementById("myImage");
        img.src = 'light-off.jpg';
    });

    document.getElementById('1').addEventListener('click', function(f) {
        let img = document.getElementById("myImage");
        img.src = 'light-on.jpg'
    });
}