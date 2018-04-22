function onload(){
    loadTabs();
}

function loadTabs(){
    console.log(18);
    urls = [
        "landing-page",
        "patients",
        "appointments",
        "tabholder"
    ]
    var pages = {};
    var elm = document.getElementById(urls[0]);

    var busyCalls = 0;
    for(var i=0;i<urls.length;i++){
        var elm = document.getElementById(urls[i]);
        var id = urls[i];
        elm = document.getElementById(id);
        function callbackGen(element, id, pages, busyCalls){
            return function(response){
                pages[id] = response;
            }
        }
        var callback = callbackGen(elm, id, pages, busyCalls);
        $.get(urls[i]+".html", callback);
    }
    $(document).ajaxStop(genBuildTabs(pages));
}

function genBuildTabs(pages){
    return function(){
        console.log(pages);
        tabHolderTemplate = Handlebars.compile(pages["tabholder"]);
        //document.getElementById("tabholder").innerHTML = tabHolderTemplate(pages);
        document.body.innerHTML = tabHolderTemplate(pages);
        console.log(4);
    }
}

//setTimeout(onload, 1000);
$( document ).ready(onload);