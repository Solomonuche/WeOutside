function signIn() {
    const userType = $('input[name=user-type]:checked').data('type');
    const formData = {
        email: $('#email').val(),
        password: $('#password').val()
    };
    
    const endPoint = getEndpoint(userType);
    const redirectUrl = getRedirectUrl(userType);
    
    $.ajax({
        type: 'POST',
        url: endPoint,
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            localStorage.setItem(`${userType}_id`, response[`${userType}_id`]);
            window.location.href = redirectUrl;
        },
        error: function(response) {

            alert(response.responseJSON.Status);
        }

    });
}

function getEndpoint(userType) {
    if (userType === 'user') {
        return 'http://127.0.0.1:5000/api/v1/users/login';
    } else if (userType === 'host') {
        return 'http://127.0.0.1:5000/api/v1/hosts/login';
    }
}
function getRedirectUrl(userType) {
    if (userType === 'user') {
        return 'user-dash.html';
    } else if (userType === 'host') {
        return 'host-dash.html';
    }
}
$('#signIn').submit((event) => {
    event.preventDefault();
    signIn();
})