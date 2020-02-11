#!/usr/bin/node
/** Script that prints the title of a Star War movie */
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  let count = 0;
  const content = JSON.parse(body);
  for (let i = 0; i < content.count; i++) {
    if (content.results[i].characters.includes('https://swapi.co/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
