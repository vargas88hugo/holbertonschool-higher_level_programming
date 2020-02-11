#!/usr/bin/node
/** Program that convert the number to a given base */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
