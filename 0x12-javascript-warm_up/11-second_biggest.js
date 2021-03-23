#!/usr/bin/node
const array = process.argv;

const newArray = [];

for (const x of array) {
  if (!isNaN(parseInt(x))) {
    newArray.push(parseInt(x));
  }
}

newArray.sort((a, b) => a - b);
newArray.pop();
console.log(newArray[newArray.length - 1]);
