#!/usr/bin/node
const Parent = require('./5-square');

// Represents the Square class, inherits from Rectangle
class Square extends Parent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
