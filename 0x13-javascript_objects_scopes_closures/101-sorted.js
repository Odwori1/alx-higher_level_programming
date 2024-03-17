#!/usr/bin/node
const data = require('./101-data');

const originalDict = data.dict;
const newDict = {};

for (const userId in originalDict) {
  const occurrence = originalDict[userId];
  if (!newDict[occurrence]) {
    newDict[occurrence] = [userId];
  } else {
    newDict[occurrence].push(userId);
  }
}

console.log(newDict);
