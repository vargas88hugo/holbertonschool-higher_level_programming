#!/usr/bin/node
/** Script that prints the title of a Star War movie */
const request = require('request');
const arg = process.argv[2];
const url = `http://swapi.co/api/films/${arg}`;

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
