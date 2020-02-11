#!/usr/bin/node
/** Program that implements function logMe */
exports.logMe = function (item) {
  if (typeof this.count === 'undefined') {
    this.count = 0;
  }

  console.log(`${this.count}: ${item}`);
  this.count++;
};
