function onload(){
    loadTabs();
}

function loadTabs(){
    urls = [
        "landing-page",
        "patients",
        "appointments",
        "tabholder",
        "entry"
    ]
    var pages = {};
    var elm = document.getElementById(urls[0]);

    var ajaxCalls = [];

    for(var i=0;i<urls.length;i++){
        var elm = document.getElementById(urls[i]);
        var id = urls[i];
        elm = document.getElementById(id);
        function callbackGen(element, id, pages){
            return function(response){
                pages[id] = response;
            }
        }
        var callback = callbackGen(elm, id, pages);
        ajaxCalls.push($.get(urls[i]+".html", callback));
    }
    $.when.apply($, ajaxCalls).then(genBuildTabs(pages));
}

function genBuildTabs(pages){
    return function(){
        tabHolderTemplate = Handlebars.compile(pages["tabholder"]);
        document.body.innerHTML = tabHolderTemplate(pages);
        //from patients.html
        loadPatients(pages);
    }
}

//setTimeout(onload, 1000);
$( document ).ready(onload);