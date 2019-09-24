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
let myCount = 0;
request(options, (err, res, body) => {
  if (err) { console.log('Error'); }
  const count = JSON.parse(body).count;
  for (let i = 0; i < count; i++) {
    const myList = JSON.parse(body).results[i].characters;
    const a = myList.filter(word => word.includes('18'));
    if (a.length > 0) {
      myCount++;
    }
  }
  console.log(myCount);
});
