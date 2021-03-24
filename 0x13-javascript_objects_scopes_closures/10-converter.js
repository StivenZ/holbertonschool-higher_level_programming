#!/usr/bin/node
exports.converter = function (base) {
  return function converterNumber (x) {
    return x.toString(base);
  };
};
