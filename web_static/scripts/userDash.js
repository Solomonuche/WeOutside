$(document).ready(function(){
    const userId = localStorage.getItem('user_id');
    const fetchDataEndpoint = 'http://127.0.0.1:5000/api/v1/users/' + userId;
    $.ajax({
        type: 'GET',
        url: fetchDataEndpoint,
        success: function(response) {
            $('#username').text(response.name);
            $('#eMail').text(response.email);
        }
    });
});