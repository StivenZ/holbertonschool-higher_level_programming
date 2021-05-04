#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const ulr = process.argv[2];
const filePath = process.argv[3];

request(ulr, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
