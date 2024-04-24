#!/usr/bin/node
// get starwars characters from a film
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(url, (error, response, body) => {
  if (error) console.log(error);
  for (const character of JSON.parse(body).characters) {
    request(character, (error, response, body) => {
      if (error) console.log(error);
      console.log(JSON.parse(body).name);
    });
  }
});
