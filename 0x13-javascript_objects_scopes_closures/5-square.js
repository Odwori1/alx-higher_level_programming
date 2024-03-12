#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Represents the Square class, inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
