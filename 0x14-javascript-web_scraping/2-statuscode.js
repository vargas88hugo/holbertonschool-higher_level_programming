#!/usr/bin/node
/** Script that display the status of a GET */
const request = require('request');
const url = process.argv[2];

request(url)
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
