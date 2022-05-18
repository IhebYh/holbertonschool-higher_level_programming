#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completed = {};
    for (const t of todos) {
      if (t.completed === true) {
        if (t.userId in completed) {
          completed[t.userId]++;
        } else {
          completed[t.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
