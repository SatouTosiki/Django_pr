// function submitForm() {
//   // result-areaのテキストを取得
//   const resultText = document.getElementById('result-area').innerText;
//   // hidden inputにテキストを設定
//   document.getElementById('result-input').value = resultText;
//   // フォームを送信
//   document.getElementById('result-form').submit();
// }



const startBtn = document.querySelector('#start-btn');
const stopBtn = document.querySelector('#stop-btn');
const resultDiv = document.querySelector('#result-area');

SpeechRecognition = webkitSpeechRecognition || SpeechRecognition;
let recognition = new SpeechRecognition();

recognition.lang = 'ja-JP';
recognition.interimResults = true;
recognition.continuous = true;

let finalTranscript = ''; // 確定した(黒の)認識結果

recognition.onresult = (event) => {
    let interimTranscript = ''; // 暫定(灰色)の認識結果
    for (let i = event.resultIndex; i < event.results.length; i++) {
        let transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
            finalTranscript += transcript;
        } else {
            interimTranscript = transcript;
        }
    }
    resultDiv.innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</i>';
}

startBtn.onclick = () => {
    recognition.start();
  }
  stopBtn.onclick = () => {
    recognition.stop();
  }