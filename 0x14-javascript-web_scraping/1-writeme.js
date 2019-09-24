#!/usr/bin/node

const args = process.argv.slice(2);
const path = args[0];
const text = args[1];
const fs = require('fs');
fs.writeFile(path, text, 'utf8', function (err) { if (err) throw err; });
