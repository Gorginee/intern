const express = require('express')

const app = express()

const bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({extended:false}));//解析 x-www-form-urlencoded
app.use(bodyParser.json());//无法演示 解析json数据依赖于urlencoded模块 必须同时应用

app.all('*', (req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'http://localhost:8080');
  res.header('Access-Control-Allow-Headers', 'X-Requested-With');
  res.header('Access-Control-Allow-Methods', 'PUT,POST,GET,DELETE,OPTIONS');
  res.header('X-Powered-By', ' 3.2.1');
  res.header('Content-Type', 'application/json;charset=utf-8');
  next();
});

app.get('/login', (req, res) => {
  const { username, password } = req.query
  if (username === 'hgj' && password === '123456') {
    res.json({ code: 0, msg: 'success'})
  } else {
    res.json({ code: 1, msg: 'failed'})
  }
  
})

app.listen(8000, () => {
  console.log('Server is running on port 8000...')
})