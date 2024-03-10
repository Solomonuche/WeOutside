$(document).ready(function(){
    const userId = localStorage.getItem('user_id');
    if (userId === null) {
        window.location.href = 'sign-in.html';
    }
    const fetchDataEndpoint = 'http://127.0.0.1:5000/api/v1/users/' + userId;
    $.ajax({
        type: 'GET',
        url: fetchDataEndpoint,
        xhrFields: {
            withCredentials: true
        },
        success: function(response) {
            $('#username').text(response.name);
            $('#eMail').text(response.email);
        }
        ,
        error: function () {
            window.location.href = 'sign-in.html';
        }
    });
    $('#signOut').on('click', function(){
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/api/v1/users/logout',
            xhrFields: {
                withCredentials: true
            },
            success: function() {
                localStorage.removeItem('user_id');
                window.location.href = 'index.html';
            },
            error: function(xhr, status, error) {
                console.error('Error during logout:', error);
                console.log(xhr);
                console.log(status);
            }
        });
    });
});