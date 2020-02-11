#!/usr/bin/node
/** Script that prints the title of a Star War movie */
const request = require('request');
const url = process.argv[2];
// const url = `http://swapi.co/api/films/`;

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  let count = 0;
  for (let i = 0; i < JSON.parse(body).count; i++) {
    if (JSON.parse(body).results[i].characters.includes('https://swapi.co/api/people/18/')) {
      count++;
      // console.log(JSON.parse(body).results[i].characters);
    }
  }
  console.log(count);
});
