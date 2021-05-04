#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');

const moviePath = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(moviePath, function (error, head) {
  if (error) {
    console.log(error);
  }
  const myDict = JSON.parse(head.body);
  console.log(myDict.title);
});
