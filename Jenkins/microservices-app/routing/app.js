const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
require('dotenv').config()

const app = express();
const port = 2998;

app.use('/user-service', createProxyMiddleware({ target: process.env.USER_SREVICE_URl,  pathRewrite: {
  [`^/user-service`]: '',
}, }));
app.use('/order-service', createProxyMiddleware({ target: process.env.ORDER_SREVICE_URl,  pathRewrite: {
  [`^/order-service`]: '',
}, }));

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})