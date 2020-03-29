const LocalStrategy = require('passport-local').Strategy;
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

//  Load User Model
const User = require('../models/User');

module.exports = function(passport) {
    passport.use('user',
        new LocalStrategy({ usernameField: 'userid' }, (userid, password, done) => {
            // Match User
            User.findOne({ userid: userid })
                .then(user => {
                    if (!user) {
                        console.log(`Mongodb: No user: ${userid} found`);
                        return done(null, false, { message: 'UserId does not exist' });
                    }
                    // Match password
                    bcrypt.compare(password, user.password, (err, isMatch) => {
                        if (err) throw err;
                        if (isMatch) {
                            if (user.type != 'user') {
                                return done(null, false, { message: 'Someone has corrupted your data' });
                            }
                            console.log('Mongodb: Login succes user: ' + user.userid);
                            require('../app').reload();
                            return done(null, user);
                        } else {
                            console.log('Mongodb: Incorrect Password user: ' + user.userid);
                            return done(null, false, { message: 'Incorrect Password' });
                        }
                    })
                })
                .catch(err => console.log(err));
        })
    );
    passport.use('admin',
        new LocalStrategy({ usernameField: 'userid' }, (userid, password, done) => {
            // Match User
            User.findOne({ userid: userid })
                .then(user => {
                    if (!user) {
                        console.log(`Mongodb: No user: ${userid} found`);
                        return done(null, false, { message: 'UserId does not exist' });
                    }
                    // Match password
                    bcrypt.compare(password, user.password, (err, isMatch) => {
                        if (err) throw err;
                        if (isMatch) {
                            if (user.type != 'admin') {
                                return done(null, false, { message: 'Someone has corrupted your data' });
                            }
                            console.log('Mongodb: Login succes user: ' + user.userid);
                            require('../app').reload();
                            return done(null, user);
                        } else {
                            console.log('Mongodb: Incorrect Password user: ' + user.userid);
                            return done(null, false, { message: 'Incorrect Password' });
                        }
                    })
                })
                .catch(err => console.log(err));
        })
    );
    passport.use('doctor',
        new LocalStrategy({ usernameField: 'userid' }, (userid, password, done) => {
            // Match User
            User.findOne({ userid: userid })
                .then(user => {
                    if (!user) {
                        console.log(`Mongodb: No user: ${userid} found`);
                        return done(null, false, { message: 'UserId does not exist' });
                    }
                    // Match password
                    bcrypt.compare(password, user.password, (err, isMatch) => {
                        if (err) throw err;
                        if (isMatch) {
                            if (user.type != 'doctor') {
                                return done(null, false, { message: 'Someone has corrupted your data' });
                            }
                            console.log('Mongodb: Login succes user: ' + user.userid);
                            require('../app').reload();
                            return done(null, user);
                        } else {
                            console.log('Mongodb: Incorrect Password user: ' + user.userid);
                            return done(null, false, { message: 'Incorrect Password' });
                        }
                    })
                })
                .catch(err => console.log(err));
        })
    );

    passport.serializeUser((user, done) => {
        done(null, user.id);
    });

    passport.deserializeUser((id, done) => {
        User.findById(id, (err, user) => {
            done(err, user);
        });
    });

}