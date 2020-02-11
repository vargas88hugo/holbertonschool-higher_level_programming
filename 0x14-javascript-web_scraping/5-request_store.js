#!/usr/bin/node
/** Script that gets the content of a webpage and stores it in a file */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(path, body, (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
