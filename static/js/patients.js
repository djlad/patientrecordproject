console.log("patient.js imported")

function loadPatients(pages){
    console.log('starting patients');
    //console.log(pages.entry);
    createEntryList(pages, 'patient');
    createEntryList(pages, 'doctor');
}

function createEntryList(pages, selectorType) {
    var holderid = selectorType+'-holder';
    $.post("/get", {
        entryType:selectorType,
        userInfo:userInfo
    }, genGetPatients(pages, holderid))
}

function genGetPatients(pages, holderid){
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
        var entryElement = document.getElementById(holderid);

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
        for(var i=1;i<listItems.length;i++) {
            li = listItems[i];
            text = li.innerText.toUpperCase();
            if (text.search(filter) === -1 && filter.length > 0){
                li.style.display = "none";
            }else{
                li.style.display = "table-row";
            }
        }
    }
}

function getPatientInfoById(id, callback){
    $.post("/getpatientbyid", {
        userInfo:userInfo,
        id:id
    }, callback)
}

function goToEditor(id, editorType){
    var editorLink = document.getElementById('editor-link');
    var editorDiv = document.getElementById('editor');
    var template = Handlebars.compile('');
    var html;
    if (editorType === "patient") {
        template = Handlebars.compile(pages['editor']);
    }
    getPatientInfoById(id, function(response){
        if (response.length > 0){
            response = response[0];
            html = template({editorType:editorType, entry:response});
            editorDiv.innerHTML = html;
        }
    });
    editorLink.click();
}

function addEntry(entryType){
    /*adds entry (ie patient, doctor) */
    $.post("/addentry", {
        userInfo:userInfo,
        entryType:entryType
    }, function(){
        console.log('patient added');
    }) 
}