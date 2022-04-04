#!/usr/bin/node

console.log(secondBig(process.argv));

function secondBig (myArray) {
  let i = 3;
  let scnd = 0;
  let max = myArray[2];
  while (i < myArray.length) {
    if (max < myArray[i]) {
      scnd = max;
      max = myArray[i];
    }
    i++;
  }
  return scnd;
}
