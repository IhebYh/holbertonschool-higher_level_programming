#!/usr/bin/node
exports.esrever = function (list) {
  let rev;
  for (let i = list.length - 1; i > 0; i--) { rev.append(list[i]); }
  return rev;
};
