#!/usr/bin/node
let num = parseInt(process.argv[2]) - 1;
if (!isNaN(num)) {
  for (; num >= 0; num--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
