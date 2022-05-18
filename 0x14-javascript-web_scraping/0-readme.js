#!/usr/bin/node

const fs = require('fs');
const Fname = process.argv[2];
fs.readFile(Fname, 'utf8', function (err, l) {
  if (err) {
    console.log(err);
  } else {
    console.log(l);
  }
});
