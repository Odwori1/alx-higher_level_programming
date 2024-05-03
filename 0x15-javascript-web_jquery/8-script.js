$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const response = data.results;
  const movie_list = $('ul#list_movies');

  for (let idx = 0; idx < response.length; idx++) {
    movie_list.append(`<li>${response[idx].title}</li>`);
  }
});