const express = require('express')

const app = express()
const port = 3000
require('dotenv').config()


var cors = require('cors')

app.use(cors())
app.use(express.json());
app.use(express.urlencoded({
  extended: true
}));

app.get('/ishu', (req, res) => {
    res.send('Hello World! From ISHU')
  })



app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
  }) 