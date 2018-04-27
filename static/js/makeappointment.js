function loadMakeAppointment(){
    buildDropDown('patient');
    buildDropDown('doctor');
}

function buildDropDown(entryType){
    getEntries(entryType, function(data) {
        for (var i=0;i<data.length;i++){
            data[i]['id'] = data[i][entryType+'ID'];
        }
        var template = Handlebars.compile(pages['select-gen']);
        var html = template({
            options:data
        });
        var dropdownelm = document.getElementById(entryType+'-drop');
        dropdownelm.innerHTML = html;
    });
}

function onMakeAppointment(){
    var appointment = {};
    input = document.getElementById('make-appointment');
    appointment.patientID = input.getElementsByTagName('select')[0].value;
    appointment.doctorID = input.getElementsByTagName('select')[1].value;
    appointment.time = input.getElementsByTagName('input')[0].value;
    appointment.location = input.getElementsByTagName('input')[1].value;
    console.log(appointment);
}

function buildPatientDoctorDropdowns(){
    
}