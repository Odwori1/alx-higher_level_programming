#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const id = process.argv[2];
request(`https://swapi-api.hbtn.io/api/films/${id}`, (error, res, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
