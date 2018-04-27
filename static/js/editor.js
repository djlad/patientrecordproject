function saveEntry(editorType){
    var editorContainer = document.getElementById('editor-inputs');
    var editorInputs = editorContainer.getElementsByTagName('input');
    var status = document.getElementById('editor-status');
    console.log('saving');

    var input;
    var keyName;
    var entry = {};
    for (let i=0;i<editorInputs.length;i++){
        input = editorInputs[i];
        keyName = input.getAttribute('data-key');
        entry[keyName] = input.value;
    }
    //entry['entryType'] = editorType;
    request = {
        entryType:editorType,
        //entry:JSON.stringify(entry),
        entry:entry,
        userInfo:userInfo
    }
    var callback = function(){
        status.innerHTML = 'save complete';
        console.log('reloaded');
        loadPatients(pages);
    }
    
    submitEntry(request, callback);
}

function submitEntry(request, callback){
    console.log(request);
    $.ajax("/save", {
        data:JSON.stringify(request),
        contentType:'application/json',
        type: 'POST',
        success: callback
    });
}