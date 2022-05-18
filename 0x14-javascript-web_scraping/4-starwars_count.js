#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
req.get(url, function (err, response, body) {
  let sum = 0;
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  for (let i = 0; data.results[i] !== undefined; ++i) {
    if (data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      sum++;
    }
  }
  console.log(sum);
});
