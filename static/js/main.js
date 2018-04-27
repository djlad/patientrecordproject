function onload(){
    loadTabs();
}

pages = {};
userInfo = {
        //username:"DanLad1",
        //password:"password1"
    }

function loadTabs(){

    urls = [
        "landing-page",
        "appointments",
        "tabholder",
        "entry",
        "editor",
        'selector-table',
        'login',
        'makeappointment',
        'select-gen'
    ]
    //pages = {};
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
        var tabHolderTemplate = Handlebars.compile(pages["tabholder"]);
        var selectorTemplate = Handlebars.compile(pages['selector-table']);
        pages['patients'] = selectorTemplate({selectorType:'patient'});
        pages['appointments'] = selectorTemplate({selectorType:'appointment'});
        pages['prescriptions'] = selectorTemplate({selectorType:'prescription'});
        pages['doctors'] = selectorTemplate({selectorType:'doctor'});
        document.body.innerHTML = tabHolderTemplate(pages);
        //from patients.html
        loadPatients(pages);
        loadLogin();
        loadMakeAppointment();
    }
}

function openModal(header, body){
    var loginModal = $('#alert-modal');
    var bodyElm = loginModal.find('p');
    var headerElm = loginModal.find('h4');
    bodyElm.text(body);
    headerElm.text(header);
    loginModal.modal();
}

Handlebars.registerHelper('if_eq', function(a, b, opts) {
    if (a == b) {
        return opts.fn(this);
    } else {
        return opts.inverse(this);
    }
});

//setTimeout(onload, 1000);
$( document ).ready(onload);