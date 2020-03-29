const mongoose = require('mongoose');
const Usertype = require('./UserType')

const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    type: {
        type: String,
        required: true
    },
    userid: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    contact: {
        type: String,
        required: false
    },
    emergency_contact: {
        type: String,
        required: false
    },
    email: {
        type: String,
        required: false
    },
    address: {
        type: String,
        required: false
    },
    address2: {
        type: String,
        required: false
    },
    city: {
        type: String,
        required: false
    },
    state: {
        type: String,
        required: false
    },
    zip: {
        type: String,
        required: false
    },
    birthdate: {
        type: String,
        required: false
    },
    gender: {
        type: String,
        required: false
    },
    date: {
        type: Date,
        default: Date.now
    }
});

const User = mongoose.model('user', UserSchema);

// TODO: only for registration 
// instead send a request to admin and he will register you as an user

User.on('save', (usr, count) => {
    const userType = new Usertype({
        user_type: 'user',
        userid: usr.userid
    });
    userType.save()
        .then(temp => {
            console.log(`Mongodb: userType saved`);
        })
        .catch(err => console.log(err));
});

module.exports = User;