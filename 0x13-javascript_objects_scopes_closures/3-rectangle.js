#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 & w > 0) {
      this.height = h;
      this.width = w;
      }
  };
  print(w, h) {
    for (let i = 0; i < this.height; i++) {
        console.log('x'.repeat(this.width));
        }
    };
}
