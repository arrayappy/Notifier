const express = require('express');
const mongoose = require('mongoose');
var mongoDB = 'mongodb://127.0.0.1/notifier';
mongoose.connect(mongoDB, { useNewUrlParser: true, useUnifiedTopology: true });
var db = mongoose.connection;
var app = express();
const auth_data = new mongoose.Schema({
    name: String,
    dob: Date,
    loves: Array,
    weight: Number,
    vampires: Number,
    gender: String,
});
const Auth = mongoose.model('Auth', auth_data);

app.get('/', (req, res) => {
    res.send('Hello, your server is running!');
});
app.get('/auth', (req, res) => {
    Auth.find({ name: 'john' }, (err, data) => {
        if (err) {
            console.log(err);
        } else {
            console.log(data[0].password);
        }
    });
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});