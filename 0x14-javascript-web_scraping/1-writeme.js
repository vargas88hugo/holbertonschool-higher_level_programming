#!/usr/bin/node
/** This script writes a script to a file */
const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, (err) => {
  if (err) {
    return console.log(err);
  }
});
