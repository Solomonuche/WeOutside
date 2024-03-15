$(document).ready(function(){
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
            let imageUrl = "http://127.0.0.1:5000/api/v1/download/hosts/" + response.image;
            $('#image').attr('src', imageUrl);
            $('#username').text(response.name);
            $('#eMail').text(response.email);
        },
        error: function () {
            window.location.href = 'sign-in.html';
        }
    });

    const hostEvents = 'http://127.0.0.1:5000/api/v1/hosts/' + hostId + '/myevents';
    // custom function to loop through event objs and add them to the dom using mustache js
    function addEvent(response, location, template) {
        $.each(response, function (index, value) {
        let text = Mustache.render(template, value);
        location.append(text);
        });
    };

    // populate my events tab for the host
    $.get(hostEvents, function (response) {
        let location = $('#menu1');
        let template = $('#template').html();
        addEvent(response, location, template);
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
                window.location.href = 'sign-in.html';
            },
            error: function () {
                window.location.href = 'sign-in.html'
            }
        });
    });
});

// delete event from host event tab 
function deleteEvent(eventID) {
    const deleteEndpoint = 'http://127.0.0.1:5000/api/v1/events/' + eventID;
    $.ajax({
        type: 'DELETE',
        url: deleteEndpoint,
        xhrFields: {
            withCredentials: true
        },
        success: function(response) {
            alert('Event deleted successfully');
            window.location.reload();
        },
        error: function () {
            alert('Error deleting event');
        }
    });
}