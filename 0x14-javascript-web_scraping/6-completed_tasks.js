#!/usr/bin/node
/** Script that computes the number of tasks completed by user id */
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  const counter = {};
  for (let i = 0; i < JSON.parse(body).length; i++) {
    if (JSON.parse(body)[i].completed === true) {
      if (counter[JSON.parse(body)[i].userId] === undefined) {
        counter[JSON.parse(body)[i].userId] = 1;
      } else {
        counter[JSON.parse(body)[i].userId]++;
      }
    }
  }
  console.log(counter);
});
