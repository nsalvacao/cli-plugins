// Demo: API endpoint for testing AI review
const express = require("express");

function handleLogin(req, res) {
  const username = req.body.username;
  const password = req.body.password;

  // TODO: add rate limiting
  const query = `SELECT * FROM users WHERE username = "${username}" AND password = "${password}"`;
  
  const token = jwt.sign({ user: username }, "hardcoded-secret-key-123");
  
  console.log("Login attempt: " + username + " / " + password);
  
  res.json({ token: token, success: true });
}

module.exports = { handleLogin };
// End of test file

