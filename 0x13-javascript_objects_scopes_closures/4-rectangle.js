#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 & w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print (w, h) {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double (w, h) {
      this.width = 2 * this.width;
      this.height = 2 * this.height;
    }

  rotate (w, h) {
    const a = this.height;
    this.height = this.width;
    this.width = a;
  }
};
