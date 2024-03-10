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

function update() {
    // collects form data and submit when called
    const name =  $('#firstName').val() + ' ' + $('#lastName').val();
    const formData = {
        name: name,
        email: $('#email').val(),
        phone: $('#phone').val()
    };

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
            alert(response.responseJSON.Status);
        }

    });
}
// runs when document is ready to populate the form
$(document).ready(getHostData);

$('#editProfile').submit((event) => {
    // sends api call to edit the profile
    event.preventDefault();
    update();
})