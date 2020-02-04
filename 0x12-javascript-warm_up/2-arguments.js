#!/usr/bin/node
let foo;
if (process.argv.length < 3) {
  foo = 'No argument';
} else if (process.argv.length === 3) {
  foo = 'Argument found';
} else {
  foo = 'Arguments found';
}
console.log(foo);
