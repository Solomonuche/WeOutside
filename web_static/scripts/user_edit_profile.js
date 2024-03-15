let userId;

function getUserData() {
    // makes api call to get user data and populate form.
    userId = localStorage.getItem('user_id');
    if (userId === null) {
        window.location.href = 'sign-in.html';
    }
    const endPoint = 'http://127.0.0.1:5000/api/v1/users/' + userId;
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

    const endPoint = 'http://127.0.0.1:5000/api/v1/users/' + userId;
    $.ajax({
        type: 'PUT',
        url: endPoint,
        data: JSON.stringify(formData),
        contentType: 'application/json',
        xhrFields: {
            withCredentials: true
        },
        success: function(response) {
            alert("Success");
            window.location.href = 'user-dash.html';
        },
        error: function(response) {
            alert(response.responseJSON.Status);
        }

    });
}
// runs when document is ready to populate the form
$(document).ready(getUserData);

$('#editProfile').submit((event) => {
    // sends api call to edit the profile
    event.preventDefault();
    let image = $('#file')[0].files[0];
    if (image) {
        // // File is selected
        uploadUserImage()
            .then((fileName) => {
                update(fileName);
            })
            .catch((error) => {
                console.error('Error uploading image:', error);
            });
    } else {
        // No file selected
        update();
    }
})

// upload user image function
function uploadUserImage() {
    return new Promise((resolve, reject) => {
        let formData = new FormData();
        let image = $('#file')[0].files[0];
        let url = 'http://127.0.0.1:5000/api/v1/upload/users';
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