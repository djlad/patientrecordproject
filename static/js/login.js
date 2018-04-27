console.log('login.js imported');

function loadLogin(){
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
            if ('invalid credentials' === response){
                openModal('Login', 'Invalid Username or Password');
            } else {
                userInfo = response;
            }
        }});
}