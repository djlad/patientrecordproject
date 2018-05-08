console.log('make prescription included')

function loadMakePrescription(){
    var makePrescriptionElm = document.getElementById('makeprescription');
    var selectPresElms = makePrescriptionElm.getElementsByTagName('select');
    var patientElm = selectPresElms[0];
    var doctorElm = selectPresElms[1];
    var prescriptionElm = makePrescriptionElm.getElementsByTagName('input')[0];
    var makePrescrBtn = makePrescriptionElm.getElementsByTagName('button')[0];
    console.log(makePrescrBtn);
    buildDropDown('patient', patientElm);
    buildDropDown('doctor', doctorElm);
    var onMakePresc = genOnMakePrescription(patientElm, doctorElm, prescriptionElm);
    makePrescrBtn.addEventListener('click', onMakePresc);
}
function genOnMakePrescription(patientElm, doctorElm, prescriptionElm){
    function onMakePrescription(){
        var patientID = patientElm.value;
        var doctorID = doctorElm.value;
        var prescriptionText = prescriptionElm.value;
        var prescription = {
            patientID:patientID,
            doctorID:doctorID,
            prescription:prescriptionText
        };
    
        var request = {
            entryType:'prescription',
            entry:prescription,
            userInfo:userInfo
        }

        function callback(resp){
            loadPatients(pages);
            openModal('Prescription Status', 'Prescription Added Successfully');
        }
        submitEntry(request, callback)
    }
    return onMakePrescription;
}