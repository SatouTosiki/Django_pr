
window.onload = function(){



const aiGenerate = document.getElementById('ai-Generate');
const sendButton = document.getElementById('sendbutton');

// MutationObserverのコールバック関数を定義
const observerCallback = (mutationsList, observer) => {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            const text = aiGenerate.textContent.trim();
            if (text) {
                sendButton.classList.remove('hidden');
            } else {
                sendButton.classList.add('hidden');
            }
        }
    }
};

// MutationObserverのインスタンスを作成
const observer = new MutationObserver(observerCallback);

// 監視の設定
const config = { childList: true, subtree: true };

// 監視を開始
observer.observe(aiGenerate, config);

}