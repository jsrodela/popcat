let count = document.getElementById('count');
let socket = new WebSocket('ws://' + window.location.host + '/ws')

socket.onmessage = (e) => {
    if(e.data.length == 1 && e.data[0] == 'W') {
        let win = document.getElementById('win');
        win.innerHTML = 'You Won!';
    }
    else {
        count.innerHTML = e.data;
    }
}

let btn = document.getElementById('btn');
btn.onclick = (e) => {
    socket.send(1);
}
// let t = setInterval(() => document.getElementById('btn').click(), 100)
