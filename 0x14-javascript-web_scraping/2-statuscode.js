#!/usr/bin/node

const request = require('request');
const ulr = process.argv[2];

request(ulr, function (error, response) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});
