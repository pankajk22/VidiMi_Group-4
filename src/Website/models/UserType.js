const mongoose = require('mongoose');

const UserTypeSchema = new mongoose.Schema({
    user_type: {
        type: String,
        required: true
    },
    userid: {
        type: String,
        required: true,
        unique: true
    },
    date: {
        type: Date,
        default: Date.now
    }
});

const UserType = mongoose.model('readOnlyUserInfo', UserTypeSchema);

module.exports = UserType;