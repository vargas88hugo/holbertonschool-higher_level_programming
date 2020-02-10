#!/usr/bin/node
/** Program that implements Square Class */
const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 1; i <= this.height; i++) {
        for (let j = 1; j <= this.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
