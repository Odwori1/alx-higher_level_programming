#!/usr/bin/node
// Script that counts the num of movies where char "Wedge Antilles" is present.
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeAntillesFilms = films.filter((film) => {
      const characters = film.characters;
      return characters.some((character) => character.includes('/18/'));
    });
    console.log(wedgeAntillesFilms.length);
  }
});
