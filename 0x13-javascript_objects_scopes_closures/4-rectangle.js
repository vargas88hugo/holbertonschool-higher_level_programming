#!/usr/bin/node
/** Program that implements Rectangle Class */
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 &&
        (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    this.temp = this.width;
    this.width = this.height;
    this.height = this.temp;
    delete this.temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
