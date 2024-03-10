function signUp() {
    // collects form data and submit when called
    const userType = $('input[name=user-type]:checked').data('type');
    const name =  $('#firstName').val() + ' ' + $('#lastName').val();
    const confirmPassword = $('#confirmPassword').val();
    const formData = {
        name: name,
        email: $('#email').val(),
        phone: $('#phone').val(),
        password: $('#password').val(),
    };

    if (formData.password !== confirmPassword) {
        alert("Passwords do not match. Please re-enter your password.");
        return;
    }

    const endPoint = getEndpoint(userType);
    $.ajax({
        type: 'POST',
        url: endPoint,
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            alert("Account created, Please sign-in,");
            window.location.href = 'sign-in.html';
        },
        error: function(response) {
            alert(response.responseJSON.Status);
        }

    });
}


function getEndpoint(userType) {
    // gets the necessary endpoint for the api call depending on usertype
    if (userType === 'user') {
        return 'http://127.0.0.1:5000/api/v1/users';
    } else if (userType === 'host') {
        return 'http://127.0.0.1:5000/api/v1/hosts';
    }
}

$('#signUp').submit((event) => {
    event.preventDefault();
    signUp();
})