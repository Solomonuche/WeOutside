$(function () {
  // Event page handling jquery
  let queryParams = new URLSearchParams(window.location.search);
  let eventID = queryParams.get('eventID');
  let template = $('#temp').html();
  let url = ' http://127.0.0.1:5000/api/v1/events/' + eventID;

  $.get(url, function (response) {
    let text = Mustache.render(template, response);
    $('#event-tab').append(text);
  });

  // display navbar for host
  const hostId = localStorage.getItem('host_id');
  const userId = localStorage.getItem('user_id');

  if (hostId) {
    let hostUrl = 'http://127.0.0.1:5000/api/v1/hosts/' + hostId;
    let template = $('#host').html();
    let location = $('#navbar');
    $.get(hostUrl, function (response) {
      let text = Mustache.render(template, response);
      location.append(text);
    });
  } else if (userId) {
      let userUrl = 'http://127.0.0.1:5000/api/v1/users/' + userId;
      let template = $('#host').html();
      let location = $('#navbar');
      $.get(userUrl, function (response) {
        let text = Mustache.render(template, response);
        location.append(text);
      });
  } else {
    $('.defualt').css("display", "block");
  }

  $('#navbar').on('click', '#signOut', function(){
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