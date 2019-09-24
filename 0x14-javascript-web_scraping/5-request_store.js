#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0];
const path = args[1];
const options = {
  url: url,
  method: 'GET',
  headers: {
    Accept: 'json',
    'Accept-Charset': 'utf-8'
  }
};

request(options, (err, res, body) => {
  if (err) {
    throw err;
  } else {
    const txt = body;
    fs.writeFile(path, txt, 'utf8', function (err) { if (err) throw err; });
  }
});
