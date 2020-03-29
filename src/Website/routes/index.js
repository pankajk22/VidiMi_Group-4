const express = require('express');
const router = express.Router();
const { ensureAuthenticated } = require('../config/auth');
const Joi = require('joi');
const fs = require('fs')
var formidable = require('formidable');


// Home page redirect to detect_in_photo
router.get('/', (req, res) => res.redirect('/detect_in_photo'));

// detect_in_photo Page
router.get('/detect_in_photo', (req, res) => res.render('detect_in_photo'));
router.post('/detect_in_photo', (req, res) => {
    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        const { zip, photo } = files;
        const schema = {
            zip: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('application/zip').required(),
                size: Joi.number().required()
            }).unknown(true).required(),
            photo: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('image/jpeg').required(),
                size: Joi.number().required()
            }).unknown(true).required()
        }
        const { error } = Joi.validate(files, schema);
        var errors = [];
        if (error != null) {
            error.details.forEach(element => {
                var message = element.message;
                errors.push(message);
            });
        }
        console.log(errors)
        if (errors.length > 0) {
            res.write(errors.toString());
            res.end();
            res.send()
        } else {
            var response = ''

            var oldpath = zip.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + zip.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Zip File uploaded and moved!\n';
            });
            var oldpath = photo.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + photo.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Photo uploaded and moved!';
                res.write(response);
                res.end();
            });
        }
    });
});

// detect_in_video Page
router.get('/detect_in_video', (req, res) => res.render('detect_in_video'));
router.post('/detect_in_video', (req, res) => {
    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        const { zip, video } = files;
        const schema = {
            zip: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('application/zip').required(),
                size: Joi.number().required()
            }).unknown(true).required(),
            video: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('video/mp4').required(),
                size: Joi.number().required()
            }).unknown(true).required()
        }
        const { error } = Joi.validate(files, schema);
        var errors = [];
        if (error != null) {
            error.details.forEach(element => {
                var message = element.message;
                errors.push(message);
            });
        }
        console.log(errors)
        if (errors.length > 0) {
            res.write(errors.toString());
            res.end();
        } else {
            var response = ''

            var oldpath = zip.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + zip.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Zip File uploaded and moved!\n';
            });
            var oldpath = video.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + video.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Video uploaded and moved!';
                res.write(response);
                res.end();
            });
        }
    });
});

// detect_hazard Page
router.get('/detect_hazard', (req, res) => res.render('detect_hazard'));
router.post('/detect_hazard', (req, res) => {
    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        const { video1, video2 } = files;
        const schema = {
            video1: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('video/mp4').required(),
                size: Joi.number().required()
            }).unknown(true).required(),
            video2: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('video/mp4').required(),
                size: Joi.number().required()
            }).unknown(true).required()
        }
        const { error } = Joi.validate(files, schema);
        var errors = [];
        if (error != null) {
            error.details.forEach(element => {
                var message = element.message;
                errors.push(message);
            });
        }
        console.log(errors)
        if (errors.length > 0) {
            res.write(errors.toString());
            res.end();
        } else {
            var response = ''

            var oldpath = video1.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + video1.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Video1 uploaded and moved!\n';
            });
            var oldpath = video2.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + video2.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Video2 uploaded and moved!';
                res.write(response);
                res.end();
            });
        }
    });
});

// get_id Page
router.get('/get_id', (req, res) => res.render('get_id'));
router.post('/get_id', (req, res) => {
    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        const { photo } = files;
        const schema = {
            photo: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('image/jpeg').required(),
                size: Joi.number().required()
            }).unknown(true).required()
        }
        const { error } = Joi.validate(files, schema);
        var errors = [];
        if (error != null) {
            error.details.forEach(element => {
                var message = element.message;
                errors.push(message);
            });
        }
        console.log(errors)
        if (errors.length > 0) {
            res.write(errors.toString());
            res.end();
        } else {
            var response = ''

            var oldpath = photo.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + photo.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Photo uploaded and moved!\n';
                res.write(response);
                res.end();
            });
        }
    });
});

// add_to_db Page
router.get('/add_to_db', (req, res) => res.render('login_page'));
router.post('/admin_login', (req, res) => res.render('add_to_db'));
router.post('/add_to_db', (req, res) => {
    var form = new formidable.IncomingForm();
    form.parse(req, function(err, fields, files) {
        const { photo } = files;
        const { userid } = fields;
        const schema = {
            photo: Joi.object({
                name: Joi.string().required(),
                path: Joi.string().required(),
                type: Joi.string().only('image/jpeg').required(),
                size: Joi.number().required()
            }).unknown(true).required()
        }
        const { error } = Joi.validate(files, schema);
        var errors = [];
        if (error != null) {
            error.details.forEach(element => {
                var message = element.message;
                errors.push(message);
            });
        }
        if (typeof(userid) == 'undefined') {
            var message = '"User Id" is required" ';
            errors.push(message);
        }
        console.log(errors)
        if (errors.length > 0) {
            res.write(errors.toString());
            res.end();
        } else {
            var response = ''

            var oldpath = photo.path;
            var newpath = '/Users/paradox/Desktop/untitled/' + photo.name;
            fs.rename(oldpath, newpath, function(err) {
                if (err) throw err;
                response += 'Photo uploaded and moved!\n';
                res.write(response);
                res.end();
            });
        }
    });
});

// help Page
router.get('/help', (req, res) => res.render('help'));

// // Dashboard
// router.get('/dashboard', ensureAuthenticated, (req, res) => {
//     if (req.user.type == 'admin')
//         res.render('dashboardAdmin', {
//             user: req.user
//         })
//     else if (req.user.type == 'user')
//         res.render('dashboardUser', {
//             user: req.user
//         })
//     else if (req.user.type == 'doctor')
//         res.render('dashboardDoc', {
//             user: req.user
//         })
// });

module.exports = router;