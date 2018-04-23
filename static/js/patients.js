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
        var entryTemplate = Handlebars.compile(pages['entry']);
        var entry = entryTemplate(pr);
        var entryElement = document.getElementById('patient-holder');

        entryElement.innerHTML = entry;

        var listItems = entryElement.getElementsByTagName("tr");
        var input = entryElement.getElementsByTagName("input")[0];
        var filterCallBack = genFilterCallback(listItems, input);
        input.addEventListener('keyup', filterCallBack);
    }
    return getPatients;
}

function genFilterCallback(listItems, input){
    return function(e){
        var filter = input.value.toUpperCase();
        var li;
        var text;
        for(var i=0;i<listItems.length;i++) {
            li = listItems[i];
            text = li.innerText.toUpperCase();
            if (text.search(filter) == -1 && filter.length > 0){
                li.style.display = "none";
            }else{
                li.style.display = "table-row";
            }
        }
    }
}