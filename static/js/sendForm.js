

function sendForm() {
    var combinedContent = document.getElementById('ai-Generate').innerText;
    document.getElementById('combined-content').value = combinedContent;
    document.getElementById('main-form').submit();
  }