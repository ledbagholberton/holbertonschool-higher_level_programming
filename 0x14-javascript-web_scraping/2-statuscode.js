#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const options = {
  url: url,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8'
  }
};

request(options, (err, res, body) => {
  if (err) { console.log('Error'); }
  console.log('code: %d', res.statusCode);
});
