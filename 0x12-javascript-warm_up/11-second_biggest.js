#!/usr/bin/node
const array = process.argv;

let newArray = [];

for (const x of array) {
  if (!isNaN(parseInt(x))) {
    newArray.push(parseInt(x));
  }
}

newArray = new Set(newArray);
newArray = Array.from(newArray);
newArray.sort((a, b) => a - b);
newArray.pop();
console.log(newArray[newArray.length - 1]);
