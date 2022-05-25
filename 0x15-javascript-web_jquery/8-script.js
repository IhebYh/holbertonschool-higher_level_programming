window.$get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach(d => {
    window.$('UL#list_movies').text('<il> ' + d.title + ' </il>');
  });
});
