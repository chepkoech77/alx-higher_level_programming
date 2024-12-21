#!/usr/bin/node
// Create a Javascript class
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h > 0) { this.width = w; this.height = h; }
  }
};
