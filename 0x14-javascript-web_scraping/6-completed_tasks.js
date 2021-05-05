#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body, algo) {
  if (error) {
    console.log(error);
    return;
  }
  const myDict = JSON.parse(body);

  const userDict = {};
  let completed = 0;
  let prevUser = 1;

  for (const i of myDict) {
    if (prevUser !== i.userId) {
      prevUser = i.userId;
      completed = 0;
    }
    if (i.completed) {
      completed++;
      userDict[i.userId] = completed;
    }
  }
  for (const tasks of Object.keys(userDict)) {
    if (userDict[tasks] === 0) {
      delete userDict.tasks;
    }
  }

  console.log(userDict);
});
