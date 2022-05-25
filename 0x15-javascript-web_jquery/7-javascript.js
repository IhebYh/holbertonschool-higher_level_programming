window.$get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  window.$('DIV#charachter').text(data.name);
});
