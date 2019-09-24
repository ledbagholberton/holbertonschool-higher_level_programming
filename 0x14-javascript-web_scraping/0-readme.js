#!/usr/bin/node

const args = process.argv.slice(2);
const path = args[0];
const fs = require('fs');
try {
  const text = fs.readFileSync(path, 'utf8');
  console.log(text);
} catch (err) {
  console.log('Error Stack', err);
  console.log('Error Code', err.code);
  console.log('Error mesage', err.message);
  console.log('Error Stack', err.stack);
  console.log('Error Errro', err.errno);
  console.log('Error Stack', err.reason);
}
