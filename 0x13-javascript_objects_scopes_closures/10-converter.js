#!/usr/bin/node
exports.converter = function (base) {
  function conversion (n) {
    return n.toString(n);
  }
  return conversion;
};
