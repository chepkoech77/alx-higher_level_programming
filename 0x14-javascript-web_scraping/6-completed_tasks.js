#!/usr/bin/node
const req = require('request');
const apiUrl = process.argv[2];

req(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  const completedTasks = {};

  data.forEach(task => {
    if (task.completed) {
        const userId = task.userId.toString();
      if (!completedTasks[userId]) {
        completedTasks[userId] = 0;
      }
      completedTasks[userId]++;
    }
  });
   let jsonString = JSON.stringify(completedTasks, null, 2);
   jsonString = jsonString.replace(/"(\d+)":/g, "'$1':"); 
   console.log(jsonString);
});
