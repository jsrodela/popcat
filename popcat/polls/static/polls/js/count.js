let count = document.getElementById('count');
let cat = document.getElementById('cat');
let close = document.getElementById('close');
let open = document.getElementById('open');
let lucky = document.getElementById('lucky');

const LUCKY_NUMBER_MESSAGE = 'NEXT LUCKY NUMBER:<br>'
let started = false;

// 웹소켓 연결 설정
const ws_protocol = location.protocol == 'https:' ? 'wss://' : 'ws://'
let socket = new WebSocket(ws_protocol + window.location.host + '/ws')


// 데이터 수신 시
socket.onmessage = (e) => {
    if(e.data[0] == 'W') {
        location.href = '/win?secret=' + e.data.substring(1);
    }
    else {
        count.innerHTML = e.data;
    }
}


// 팝캣 클릭 시
function catClick(isOpen) {
    open.hidden = !isOpen;
    close.hidden = isOpen;
}

cat.onclick = (e) => {
    if(!started) {
        started = true;
        lucky.innerHTML = LUCKY_NUMBER_MESSAGE + '0';
    }
    socket.send(1);

    new Audio(sound_src).play();
    catClick(true);
    setTimeout(() => catClick(false), 300);
}
// let t = setInterval(() => document.getElementById('btn').click(), 100)
