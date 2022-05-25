window.$(this).ready(function () {
  window.$('INPUT#btn_translate').on('click', function () {
    window.$getJSON('https://fourtonfish.com/hellosalut/hello/' + window.$('INPUT#language_code').val(), function (data) {
      window.$('DIV#hello').text(data.hello);
    });
  });
  window.$('INPUT#language_code').keyup(function (e) {
    if (e.keyCode === 13) {
      window.$getJSON('https://fourtonfish.com/hellosalut/hello/' + window.$(this).val(), function (data) {
        window.$('DIV#hello').text(data.hello);
      });
    }
  });
});
