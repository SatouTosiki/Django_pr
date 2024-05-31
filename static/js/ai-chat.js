
  function getContent() {
    // resultのテキストを取得
    var resultText = document.getElementById('result-area').innerText;
    // 入力値を取得
    var userInput = document.getElementById('user-chat').value;

    // 取得した内容をコンソールに表示（テスト用）
    console.log('Result:', resultText);
    console.log('User Input:', userInput);

    // 取得した内容をページ上の特定の場所に表示する場合
    document.getElementById('ai-Generate').innerHTML = 
    resultText  + userInput  



}
