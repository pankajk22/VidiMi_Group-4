const mongoose = require('mongoose');

const PrescriptionSchema = new mongoose.Schema({
    p_details: {
        type: JSON,
        required: true
    },
    d_details: {
        type: JSON,
        required: true
    },
    vitals: {
        type: JSON,
        required: true
    },
    symptoms: {
        type: String,
        required: true
    },
    advice: {
        type: String,
        required: true
    },
    disease: {
        type: Array,
        required: true,
        default: []
    },
    medicines: {
        type: Array,
        required: true,
        default: []
    },
    tests: {
        type: Array,
        required: true,
        default: []
    },
    date: {
        type: Date,
        default: Date.now
    }
});

const Prescription = mongoose.model('prescription', PrescriptionSchema);

module.exports = Prescription;