$(document).ready(function(){
    const hostId = localStorage.getItem('host_id');
    const fetchDataEndpoint = 'http://127.0.0.1:5000/api/v1/hosts/' + hostId;
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
    });
    $('#signOut').on('click', function(){
        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/api/v1/hosts/logout',
            xhrFields: {
                withCredentials: true
            },
            success: function() {
                localStorage.removeItem('host_id');
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