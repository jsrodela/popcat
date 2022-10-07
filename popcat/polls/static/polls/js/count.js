let count = document.getElementById('count');
let cat = document.getElementById('cat');
let close = document.getElementById('close');
let open = document.getElementById('open');
let lucky = document.getElementById('lucky');

const LUCKY_NUMBER = 'NEXT LUCKY NUMBER:<br>'
let socket = new WebSocket('ws://' + window.location.host + '/ws')
let started = false;

socket.onmessage = (e) => {
    if(e.data.length == 1 && e.data[0] == 'W') {
        location.href = '/win'
    }
    else {
        count.innerHTML = e.data;
    }
}

function catClick(isOpen) {
    open.hidden = !isOpen;
    close.hidden = isOpen;
}

cat.onclick = (e) => {
    if(!started) {
        started = true;
        lucky.innerHTML = LUCKY_NUMBER + '0';
    }
    socket.send(1);

    new Audio(sound_src).play();
    catClick(true);
    setTimeout(() => catClick(false), 300);
}
// let t = setInterval(() => document.getElementById('btn').click(), 100)
