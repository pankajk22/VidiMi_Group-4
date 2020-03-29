const MongoURIarr = ['mongodb://loginHospital:qtynd67enxj@localhost:27017/HospitalManagment', 'mongodb://adminHospital:yusatf76tdvg7qw@localhost:27017/HospitalManagment'];
const MongoURI = MongoURIarr[1];

module.exports = {
    MongoURI,
    getUri: () => { return MongoURI }
}

/* NOTE: Admin can read write any data */

// db.createUser({ user: "adminHospital", pwd: "yusatf76tdvg7qw", roles: [{ role: "readWrite", db: "HospitalManagment" }, { role: "readWrite", db: "HospitalPrescriptions" }] })

/* NOTE: User before any login can read all the users data */

// db.createRole({
//     role: "readAllUserData",
//     privileges: [
//         { resource: { db: "HospitalManagment", collection: "" }, actions: ["find"] }
//     ],
//     roles: []
// })
// db.createUser({ user: "loginHospital", pwd: "qtynd67enxj", roles: [{ role: "readAllUserData", db: "HospitalManagment" }] })

/* NOTE: User after login can only update its basic data */

// db.createRole({
//     role: "updateOnlyBasicUserData",
//     privileges: [
//         { resource: { db: "HospitalManagment", collection: "users" }, actions: ["update"] }
//     ],
//     roles: []
// })

// db.createUser({ user: "afterLoginHospital", pwd: "234edfgcrtyq3r", roles: [{ role: "updateOnlyBasicUserData", db: "HospitalManagment" }] })