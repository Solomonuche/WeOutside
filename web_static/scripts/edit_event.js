let queryParams = new URLSearchParams(window.location.search);
let eventID = queryParams.get('eventID');
let url = ' http://127.0.0.1:5000/api/v1/events/' + eventID;

$(function () {
    // render event edit form    
    let template = $('#editTemp').html();
    
    $.get(url, function (response) {
        let text = Mustache.render(template, response);
        $('#edit').append(text);
    });
    
    $('#edit').on('submit', '#editEvent', (event) => {
        event.preventDefault();
        let image = $('#file')[0].files[0];
        if (image) {
            // // File is selected
            uploadEventImage()
                .then((fileName) => {
                    editEvent(fileName);
                })
                .catch((error) => {
                    console.error('Error uploading image:', error);
                });
            // alert('image file detected')
        } else {
            // No file selected
            editEvent();
            // alert('No image file detected')
        }
    });
});

let hostId
function editEvent(fileName='') {
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
        description: $('#about').val()
    };
    // validate datetime value to prevent passing empty string
    if (dateTime[0]) {
        formDate.date = dateTime[0];
    }

    if (dateTime[1]) {
        formDate.time = dateTime[1];
    }

    if (fileName) {
        formData.image = fileName;
    }

    $.ajax({
        type: 'PUT',
        url: url,
        xhrFields: {
            withCredentials: true
        },
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            alert("Event edited successfully");
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
