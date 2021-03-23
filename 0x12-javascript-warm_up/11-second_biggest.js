#!/usr/bin/node
const array = process.argv;
const tamaño = process.argv.length;

if (tamaño === 2 && tamaño === 3) {
  console.log(0);
} else {
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
}
