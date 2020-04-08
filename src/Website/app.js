const express = require('express');
const expressLayouts = require('express-ejs-layouts');
const mongoose = require('mongoose');
const flash = require('connect-flash');
const session = require('express-session');
const passport = require('passport');

const app = express();

// static files
app.use(express.static("public"));


// Website icon
var favicon = require('serve-favicon');
app.use(favicon(__dirname + '/public/images/icons/doctor.png'));

// Passport config 
require('./config/passport')(passport);

// Mongodb config
const db = require('./config/keys');

// Connect to Mongo
// var connectionURI = db.getUri();
// mongoose.connect(connectionURI, { useCreateIndex: true, useNewUrlParser: true, useUnifiedTopology: true })
//     .then(() => console.log("Mongodb: Connected.."))
//     .catch(err => console.log(err));
// module.exports = {
//     reload: () => {
//         mongoose.disconnect();
//         connectionURI = db.getUri();
//         mongoose.connect(connectionURI, { useCreateIndex: true, useNewUrlParser: true, useUnifiedTopology: true })
//             .then(() => console.log("Mongodb: Connection reloded.."))
//             .catch(err => console.log(err));
//     }
// }

// EJS
app.use(expressLayouts);
app.set('view engine', 'ejs');

// Bodyparser
app.use(express.urlencoded({ extended: false }));

// Express Session
app.use(session({
    secret: 'secrect',
    resave: true,
    saveUninitialized: true
}));

// Passport middleware
app.use(passport.initialize());
app.use(passport.session());

// Connect flash
app.use(flash());

// Global Vars
app.use((req, res, next) => {
    res.locals.success_msg = req.flash('success_msg');
    res.locals.error_msg = req.flash('error_msg');
    res.locals.error = req.flash('error');
    next();
})

// Routes
app.use('/', require('./routes/index'));

// // users.js
// app.use('/users', require('./routes/users'));

// // doctor.js
// app.use('/doctor', require('./routes/doctors'));

// // search.js
// app.use('/search', require('./routes/search'));


const port = process.env.PORT || 3004;
app.listen(port, () => console.log(`listing to port ${port}...`));