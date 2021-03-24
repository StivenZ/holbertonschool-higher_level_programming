#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const tamaño = list.length;
  let contador = 0;

  for (let i = 0; i < tamaño; i++) {
    if (list[i] === searchElement) {
      contador++;
    }
  }
  return contador;
};
