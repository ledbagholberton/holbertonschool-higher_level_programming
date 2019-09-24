#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length; i > 0; i--) {
    reversed[i - 1] = list[list.length - i];
  }
  return (reversed);
};
