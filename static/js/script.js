document
  .getElementById('user_input')
  .addEventListener('keydown', function (event) {
    if (event === 'enter') {
      // 13 represents the Enter key
      event.preventDefault(); // Prevent form submission
      document.getElementById('chat-form').submit(); // Manually submit the form
    }
  });
