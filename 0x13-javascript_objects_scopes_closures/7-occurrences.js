#!/usr/bin/node
// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let idx = 0; idx < list.length; idx++) {
    if (list[idx] === searchElement) {
      count++;
    }
  }
  return count;
};
