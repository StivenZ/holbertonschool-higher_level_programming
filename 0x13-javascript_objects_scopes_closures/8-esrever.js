#!/usr/bin/node
exports.esrever = function (list) {
  const tamaño = list.length;
  const reversed = [];
  for (let i = tamaño - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
