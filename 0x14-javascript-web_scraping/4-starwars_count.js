#!/usr/bin/node
const req = require('request');
const apiUrl = process.argv[2];

const wedgeAntillesId = 'https://swapi-api.alx-tools.com/api/people/18/';

req(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const movies = data.results.filter(
    film => film.characters.includes(wedgeAntillesId));
  console.log(movies.length);
});
