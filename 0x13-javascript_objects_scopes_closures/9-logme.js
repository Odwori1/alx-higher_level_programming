#!/usr/bin/node
// prints the number of args already printed and the new arg value
exports.logMe = function (item) {
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  } else {
    exports.logMe.count++;
  }
  console.log(exports.logMe.count + ': ' + item);
};
