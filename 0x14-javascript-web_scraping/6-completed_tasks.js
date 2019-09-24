#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const url = args[0];
const options = {
  url: url,
  method: 'GET',
  headers: {
    Accept: 'json',
    'Accept-Charset': 'utf-8'
  }
};
let my_dict = {};
request(options, (err, res, body) => {
  if (err) { throw err;
  } else {
  myList = JSON.parse(body);
  myList.forEach(function(element) {
    if (element.completed === 'true') {
      if (element.userId
   

  console.log(txt);
  }
});
