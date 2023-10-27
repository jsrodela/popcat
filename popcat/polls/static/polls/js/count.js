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

let next_lucky_number = '0'

// 데이터 수신 시
socket.onmessage = (e) => {
    if(e.data[0] == 'W') {
        location.href = '/win?secret=' + e.data.substring(1);
    }
    else if(e.data[0] == 'L') {
        next_lucky_number = e.data.substring(1);
        if (started) {
            lucky.innerHTML = LUCKY_NUMBER_MESSAGE + next_lucky_number;
        }
    }
    else {
        if (parseInt(e.data) > parseInt(count.innerHTML)) {
            count.innerHTML = e.data;
        }
    }
}

socket.onclose = (e) => {
    alert('⚠️ 서버와 연결이 끊겼습니다. 새로고침하여 다시 연결해주세요.')
}

// 팝캣 클릭 시
function changeImage(isOpen) {
    open.hidden = !isOpen;
    close.hidden = isOpen;
}

function catClick() {
    if(!started) {
        started = true;
        lucky.innerHTML = LUCKY_NUMBER_MESSAGE + next_lucky_number;
    }
    socket.send(1);

    new Audio(sound_src).play();
    changeImage(true);
    count.innerHTML = parseInt(count.innerHTML)+1;
    setTimeout(() => changeImage(false), 300);
}

if ("ontouchstart" in document.documentElement) {
    cat.addEventListener("touchstart", catClick);
}
else {
    cat.addEventListener("click", catClick);
}

// let t = setInterval(() => document.getElementById('btn').click(), 100)
