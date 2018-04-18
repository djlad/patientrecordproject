function onload(){
    loadTabs();
}

function loadTabs(){
    console.log(18);
    urls = [
        "landing-page",
        "patients",
        "appointments"
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
                element.innerHTML = response;
                pages[id] = response;
                busyCalls--;
                console.log(busyCalls);
            }
        }
        var callback = callbackGen(elm, id, pages, busyCalls);
        busyCalls+=1;
        $.get(urls[i]+".html", callback);
    }
}

setTimeout(onload, 1000);
//$( document ).ready(onload);