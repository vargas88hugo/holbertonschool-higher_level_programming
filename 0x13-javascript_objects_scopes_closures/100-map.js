#!/usr/bin/node
/** script that imports an array and computes a new array */
const list = require('./100-data').list;
console.log(list);
console.log(list.map((value, index) => value * index));
