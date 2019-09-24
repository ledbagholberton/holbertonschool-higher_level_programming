#!/usr/bin/node

let number = 0;
exports.logMe = function (item) {
  number++;
  console.log(number + ' : ' + item);
};
