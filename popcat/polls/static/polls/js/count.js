let count = document.getElementById('count');
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

let cat = document.getElementById('cat');
let lucky = document.getElementById('lucky');
const LUCKY_NUMBER = 'NEXT LUCKY NUMBER:<br>'

cat.onclick = (e) => {
    if(!started) {
        started = true;
        lucky.innerHTML = LUCKY_NUMBER + '0';
    }
    socket.send(1);
}
// let t = setInterval(() => document.getElementById('btn').click(), 100)
