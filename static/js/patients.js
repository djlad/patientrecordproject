console.log("patient.js imported")

function loadPatients(pages){
    console.log('starting patients');
    //console.log(pages.entry);
    createPatientsList(pages);
}

function createPatientsList(pages) {
    $.post("/getpatients", {
        username:"DanLad1",
        password:"password1"
    }, genGetPatients(pages))
}
function genGetPatients(pages){
    function getPatients(patientsResponse){
        var headers = [];
        if (patientsResponse.length > 0){
            headers = Object.keys(patientsResponse[0]);
        }
        pr = {
            entries:patientsResponse,
            headers:headers
        };
        console.log(patientsResponse);
        console.log('hi');
        var entryTemplate = Handlebars.compile(pages['entry']);
        var entry = entryTemplate(pr);
        console.log(pr);
        console.log(entry);
        document.getElementById('patient-holder').innerHTML = entry;
    }
    return getPatients;
}