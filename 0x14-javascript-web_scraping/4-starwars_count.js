#!/usr/bin/node

const moviePath = process.argv[2];
const request = require('request');
let numPelis = 0;

request(moviePath, function (error, head) {
  if (error) {
    console.log(error);
  }
  const myDict = JSON.parse(head.body);

  for (const peli in myDict.results) {
    for (const char in myDict.results[peli].characters) {
      const url = myDict.results[peli].characters[char].split('/');
      if (url.includes('18')) {
        numPelis++;
      }
    }
  }
  console.log(numPelis);
});
