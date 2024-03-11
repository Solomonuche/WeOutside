let hostId
function createEvent() {
    // collects form data and submit when called
    hostId = localStorage.getItem('host_id');
    if (hostId === null) {
        window.location.href = 'sign-in.html';
    }
    const dateTime = $('#dateTime').val().split('T');
    const formData = {
        name: $('#ename').val(),
        city: $('#city').val(),
        venue: $('#location').val(),
        date: dateTime[0],
        time: dateTime[1],
        description: $('#about').val()
    };

    const endPoint = 'http://127.0.0.1:5000/api/v1/hosts/' + hostId + '/events';
    $.ajax({
        type: 'POST',
        url: endPoint,
        xhrFields: {
            withCredentials: true
        },
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            alert("Event Created,");
            window.location.href = 'host-dash.html';
        },
        error: function(response) {
            console.log(response);
        }

    });
}

$('#createEvent').submit((event) => {
    event.preventDefault();
    createEvent();
});
$(document).ready(function(){
    //populates the side nav bar
    const hostId = localStorage.getItem('host_id');
    if (hostId === null) {
        window.location.href = 'sign-in.html';
    }
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
        },
        error: function () {
            window.location.href = 'sign-in.html';
        }
    });
});