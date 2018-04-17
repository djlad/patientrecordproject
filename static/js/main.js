function onload(){
    loadTabs();
}

function loadTabs(){
    console.log(18);
    urls = [
        "landing-page",
        "patients"
    ]
    var elm = document.getElementById(urls[0]);

    for(var i=0;i<urls.length;i++){
        $.get(urls[i]+".html", (response)=>{
            var elm = document.getElementById(urls[i]);
            var id = urls[i];
            console.log(id)
            elm = document.getElementById(id);
            console.log(elm);
            console.log('hi');
        });
    }
}

$( document ).ready(onload);