console.log('login.js imported');

function loadLogin(){
    console.log(userInfo);
}

function onLogin(){
    var username = document.getElementById('username-input').value;
    var password = document.getElementById('password-input').value;
    var url = '/login';
    request = {
        username:username,
        password:password
    }
    $.ajax("/login", {
        data:JSON.stringify(request),
        contentType:'application/json',
        type: 'POST',
        success: function(response){
            console.log(response)
            if ('invalid credentials' === response){
                console.log('invalidated');
                var loginModal = document.getElementById('login-modal');
                console.log(loginModal);
            } else {
                userInfo = response;
            }
        }});
}