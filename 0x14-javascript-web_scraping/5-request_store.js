#!/usr/bin/node
const req = require('request');
const fs = require('fs');

const filePath = process.argv[3];
const url = process.argv[2];

req(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
