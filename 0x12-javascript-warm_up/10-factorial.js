#!/usr/bin/node
const x = parseInt(process.argv[2]);

function factorial (y) {
  if (y === 1 || isNaN(y)) {
    return 1;
  } else {
    return (y * factorial(y - 1));
  }
}

console.log(factorial(x));
