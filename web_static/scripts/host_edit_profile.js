let hostId;

function getHostData() {
    // makes api call to get user data and populate form.
    hostId = localStorage.getItem('host_id');
    if (hostId === null) {
        window.location.href = 'sign-in.html';
    }
    const endPoint = 'http://127.0.0.1:5000/api/v1/hosts/' + hostId;
    $.ajax({
        type: 'GET',
        url: endPoint,
        xhrFields: {
            withCredentials: true
        },
        success: function(response) {
            // splits name field and feeds data to form
            const name = response.name.split(' ');
            $('#firstName').val(name[0]);
            $('#lastName').val(name[1]);
            $('#email').val(response.email);
            $('#phone').val(response.phone);
        }
    });

}

function update(fileName='') {
    // collects form data and submit when called
    const name =  $('#firstName').val() + ' ' + $('#lastName').val();
    const formData = {
        name: name,
        email: $('#email').val(),
        phone: $('#phone').val()
    };

    if (fileName) {
        formData.image = fileName;
    }

    const endPoint = 'http://127.0.0.1:5000/api/v1/hosts/' + hostId;
    $.ajax({
        type: 'PUT',
        url: endPoint,
        xhrFields: {
            withCredentials: true
        },
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            alert("Success");
            window.location.href = 'host-dash.html';
        },
        error: function(response) {
            //alert(response.responseJSON.Status);
            $('.spinner-border').css('display', 'none');
            alert('Error editing profile. Pls ensure you have an active internet connection and try again.');
        }

    });
}
// runs when document is ready to populate the form
$(document).ready(getHostData);

$('#editProfile').submit((event) => {
    // sends api call to edit the profile
    event.preventDefault();
    $('.spinner-border').css('display', 'inline-block');
    let image = $('#file')[0].files[0];
    if (image) {
        // // File is selected
        uploadHostImage()
            .then((fileName) => {
                update(fileName);
            })
            .catch((error) => {
                $('.spinner-border').css('display', 'none');
                alert('Error uploading image. Pls ensure you have an active internet connection or image is a .jpg or .jpeg or .png file');
            });
    } else {
        // No file selected
        update();
    }
})

// upload user image function
function uploadHostImage() {
    return new Promise((resolve, reject) => {
        let formData = new FormData();
        let image = $('#file')[0].files[0];
        let url = 'http://127.0.0.1:5000/api/v1/upload/hosts';
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

$('.signOut').on('click', function(){
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