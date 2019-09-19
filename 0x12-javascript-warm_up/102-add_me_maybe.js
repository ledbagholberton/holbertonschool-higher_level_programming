#!/usr/bin/node
// Function that increment and call
exports.addMeMaybe = function (number, thefunction) {
  thefunction(number++);
};
