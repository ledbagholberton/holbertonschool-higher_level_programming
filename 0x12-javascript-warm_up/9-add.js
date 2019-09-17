#!/usr/bin/node
// Add numbers
const args = process.argv.slice(2);
const a = args[0];
const b = args[1];
console.log(add(a, b));

function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
