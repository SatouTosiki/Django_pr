function submitForm() {
  // result-areaのテキストを取得
  const resultText = document.getElementById('result-area').innerText;
  // hidden inputにテキストを設定
  document.getElementById('result-input').value = resultText;
  // フォームを送信
  document.getElementById('result-form').submit();
}