#!/usr/bin/node
/** This script reads and prints the content of a file */
const fs = require('fs');
const arg = process.argv[2];

fs.readFile(arg, 'utf8', (err, contents) => {
  if (contents === undefined) {
    console.log(err);
  } else {
    process.stdout.write(contents);
  }
});
