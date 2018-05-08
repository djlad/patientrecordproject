console.log("patient.js imported")

function loadPatients(pages){
    //console.log(pages.entry);
    createEntryList(pages, 'patient');
    createEntryList(pages, 'doctor');
    createEntryList(pages, 'appointment');
    createEntryList(pages, 'prescription');
}

function getEntries(entryType, callback){
    let request = {
        entryType:entryType,
        userInfo:userInfo
    }
    $.ajax("/getentries", {
        data:JSON.stringify(request),
        contentType:'application/json',
        type: 'POST',
        success: callback
    });
}

function createEntryList(pages, selectorType) {
    var callback = genGetPatients(pages, selectorType);
    getEntries(selectorType, callback);
}

function genGetPatients(pages, selectorType){
    var holderid = selectorType+'-holder';
    var idName = selectorType+'ID';
    function getPatients(patientsResponse){
        for (var i=0;i<patientsResponse.length;i++){
            patientsResponse[i].ID = patientsResponse[i][idName];
            delete patientsResponse[i][idName];
            patientsResponse[i].selectorType = selectorType;
        }
        var headers = [];
        if (patientsResponse.length > 0){
            headers = Object.keys(patientsResponse[0]);
        }
        pr = {
            entries:patientsResponse,
            headers:headers,
            selectorType:selectorType
        };
        var entryTemplate = Handlebars.compile(pages['entry']);
        var entry = entryTemplate(pr);
        //console.log(entry);
        //console.log(pr);
        //refers to holder defined in tabholder.html
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

function getEntryById(id, entryType, callback){
    $.post("/getentrybyid", {
        userInfo:userInfo,
        id:id,
        entryType:entryType
    }, callback)
}

function goToEditor(id, editorType){
    var editorLink = document.getElementById('editor-link');
    var editorDiv = document.getElementById('editor');
    var template = Handlebars.compile(pages['editor']);
    var html;
    //editorType is same as entry type in database
    getEntryById(id, editorType, function(response){
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
    }, function(response){
        console.log(entryType + ' added');
        loadPatients(pages);
        console.log(response);
    }) 
}

function deleteEntry(id, entryType, buttonElm){
    var crow = $(buttonElm).closest('tr');
    crow.hide();
    $.post('/deleteentry',{
        userInfo:userInfo,
        ID:id,
        entryType:entryType
    }, function(){
        console.log('deleted entry');
        $(buttonElm).closest('tr').hide();
    })
}