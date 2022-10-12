window.addEventListener('load', setCatHeight);
window.addEventListener('resize', setCatHeight);

const textContainer = document.getElementById('text');
new ResizeObserver(setCatHeight).observe(textContainer);

function setCatHeight() {
    document.getElementById('cat').style.height =
        window.innerHeight -
        textContainer.offsetHeight +
        'px';
}

try {
    document.getElementById('close').ondragstart = () => {
        return false;
    };
    document.getElementById('open').ondragstart = () => {
        return false;
    };
} catch { }
