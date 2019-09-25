#!/usr/bin/node

const request = require('request');
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
const myAnswer = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };
const myDict = [];
request(options, (err, res, body) => {
  if (err) {
    throw err;
  } else {
    const myList = JSON.parse(body);
    myList.forEach(function (element) {
      if (element.completed === true) {
        myDict.push(element.userId);
      }
    });
    const myArray = Array.from(myDict);
    myArray.forEach(function (element) {
      if (element === 1) {
        myAnswer['1']++;
      }
      if (element === 2) {
        myAnswer['2']++;
      }
      if (element === 3) {
        myAnswer['3']++;
      }
      if (element === 4) {
        myAnswer['4']++;
      }
      if (element === 5) {
        myAnswer['5']++;
      }
      if (element === 6) {
        myAnswer['6']++;
      }
      if (element === 7) {
        myAnswer['7']++;
      }
      if (element === 8) {
        myAnswer['8']++;
      }
      if (element === 9) {
        myAnswer['9']++;
      }
      if (element === 10) {
        myAnswer['10']++;
      }
    });
    console.log(myAnswer);
  }
});
