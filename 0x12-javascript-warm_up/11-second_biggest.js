#!/usr/bin/node
// Second biggest numbers
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  const argssorted = args.sort(function (a, b) { return a - b; });
  console.log(argssorted[argssorted.length - 2]);
}
