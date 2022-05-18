#!/usr/bin/node

const fs = require('fs');
const Fname = process.argv[2];
const Fcontent = process.argv[3];

fs.writeFile(Fname, Fcontent, function (err) {
  if (err) {
    console.log(err);
  }
});
