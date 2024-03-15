let hostId
function createEvent(fileName) {
    // collects form data and submit when called
    hostId = localStorage.getItem('host_id');
    if (hostId === null) {
        window.location.href = 'sign-in.html';
    }
    const dateTime = $('#dateTime').val().split('T');
    const formData = {
        image: fileName,
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

function uploadEventImage() {
    return new Promise((resolve, reject) => {
        let formData = new FormData();
        let image = $('#file')[0].files[0];
        let url = 'http://127.0.0.1:5000/api/v1/upload';
        formData.append('file', image);

        $.ajax({
            url: url,
            type: 'POST',
            xhrFields: {
                withCredentials: true
            },
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                let fileName = response.filename;
                resolve(fileName);
            },
            error: function(xhr, status, error) {
                reject(error);
            }
        });
    });
}

$('#createEvent').submit((event) => {
    event.preventDefault();
    uploadEventImage()
        .then((fileName) => {
            createEvent(fileName);
        })
        .catch((error) => {
            console.error('Error uploading image:', error);
        });
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
            let imageUrl = "http://127.0.0.1:5000/api/v1/download/users/" + response.image;
            $('#image').attr('src', imageUrl);
            $('#username').text(response.name);
            $('#eMail').text(response.email);
        },
        error: function () {
            window.location.href = 'sign-in.html';
        }
    });
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