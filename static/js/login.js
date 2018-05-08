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
                $(".user-drop").hide();
                userInfo = response;
                openModal('Login',
                'You have successfully logged in as a '+userInfo.userType);

                var userTypeToDrop = ['Patient', 'Nurse', 'Doctor', 'Admin'];
                loadPatients(pages);
                $(".user-drop").eq(userTypeToDrop.indexOf(userInfo.userType)).show();
            }
        }});
}