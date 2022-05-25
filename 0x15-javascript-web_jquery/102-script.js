window.$(this).ready(function () {
  window.$('INPUT#btn_translate').on('click', function () {
    window.$getJSON('https://fourtonfish.com/hellosalut/hello/' + window.$('INPUT#language_code').val(), function (data) {
      window.$('DIV#hello').text(data.hello);
    });
  });
});
