#!/usr/bin/node
// Function that increment and call
exports.addMeMaybe = function (number, thefunction) {
  number = number + 1;
  thefunction(number);
};
