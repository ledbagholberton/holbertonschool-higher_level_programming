#!/usr/bin/node

const args = process.argv.slice(2);
const path = args[0];
const fs = require('fs');

try {
  const text = fs.readFileSync(path, 'utf8');
  console.log(text);
} catch (err) {
//  const myDict = { 'Error: ': err.message, 'errno: ': err.errno, 'code: ': err.code, 'syscall: ': err.syscall, 'path: ': path };
  console.log(err);
}
