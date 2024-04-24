#!/usr/bin/node
// Script to print all characters of a Star Wars movie based on Movie ID.
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    function fetchCharacterName (url) {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    }

    async function printCharacterNames () {
      for (const characterUrl of characters) {
        try {
          const characterName = await fetchCharacterName(characterUrl);
          console.log(characterName);
        } catch (err) {
          console.error(err);
        }
      }
    }
    printCharacterNames();
  }
});
