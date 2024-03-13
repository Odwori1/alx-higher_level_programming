#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (error, data) => {
  if (error) throw error;
  let content = data.toString();
  fs.readFile(process.argv[3], (error, data) => {
    if (error) throw error;
    content += data.toString();
    fs.writeFile(process.argv[4], content, (error) => {
      if (error) throw error;
    });
  });
});
