#!/usr/bin/node
// script that imports an array and computes a new array.
const data = require('./100-data');

const originalList = data.list;
const newList = originalList.map((value, index) => value * index);

console.log(originalList);
console.log(newList);
