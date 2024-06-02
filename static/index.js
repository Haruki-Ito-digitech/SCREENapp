const videoElem = document.getElementById("video");
const startElem = document.getElementById("start");
const stopElem = document.getElementById("stop");

// Options for getDisplayMedia()
var displayMediaOptions = {
    video: {
        cursor: "always"
    },
    audio: false
};

// Set event listeners for the start and stop buttons
startElem.addEventListener("click", function (evt) {
    startCapture();
}, false);

stopElem.addEventListener("click", function (evt) {
    stopCapture();
}, false);

async function startCapture() {
    try {
        videoElem.srcObject = await navigator.mediaDevices.getDisplayMedia(displayMediaOptions);
    } catch (err) {
        console.error("Error: " + err);
    }
}

function stopCapture(evt) {
    let tracks = videoElem.srcObject.getTracks();

    tracks.forEach(track => track.stop());
    videoElem.srcObject = null;
}


// ソケット通信を使うための宣言
const socket = io.connect('/demo')

// サーバーのデータを読み込み
socket.on('message', (data) => {
    console.log('message', data)
    const li = document.createElement('li')
    li.appendChild(document.createTextNode(data))
    document.getElementById('messages').appendChild(li)
})

// 送信ボタンをクリックした時
document.getElementById('send').addEventListener('click', (e) => {
    const message_input = document.getElementById('message_input')
    const message = message_input.value
    // クライアントからサーバーへ送信
    socket.emit('message', message)
    message_input.value = ''
})

// enterを押したとき
document.getElementById('message_input').addEventListener('keydown', (e) => {
    if (e.keyCode === 13) {
        const message_input = document.getElementById('message_input')
        const message = message_input.value
        // クライアントからサーバーへ送信
        socket.emit('message', message)
        message_input.value = ''
    }
})
    