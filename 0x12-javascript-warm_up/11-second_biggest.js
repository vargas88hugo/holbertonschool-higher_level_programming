#!/usr/bin/node
let biggest = 0;
let i;
const arr = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    arr[i - 2] = parseInt(process.argv[i]);
  }
}

if (arr.length > 1) {
  biggest = Math.max.apply(null, arr);
  i = arr.indexOf(biggest);
  arr[i] = -Infinity;
  biggest = Math.max.apply(null, arr);
}

console.log(biggest);
