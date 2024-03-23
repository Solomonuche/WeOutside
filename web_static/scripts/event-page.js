function addEvent(response, location, template, count = 0) {
  // custom function to loop through event objs and add them to the dom using mustache js
  let i = 0;
  $.each(response, function (index, value) {
    // count determine how many times the event object is added to the DOM
    if (count !== 0 && i === count) {
      return false;
    };
    let text = Mustache.render(template, value);
    location.append(text);
    i++;
  });
}

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
  let reviewUrl = `http://127.0.0.1:5000/api/v1/events/${eventID}/reviews`;
  $.get(reviewUrl, function (response) {
    let temp = $('#comments').html();
    let loc = $('#home');
    addEvent(response, loc, temp, count=4);

  });
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
  function comment() {
    const formData = {
        description: $('#about').val()
    };
    let queryParams = new URLSearchParams(window.location.search);
    let eventID = queryParams.get('eventID');
    const endPoint = `http://127.0.0.1:5000/api/v1/events/${eventID}/reviews`;
    $.ajax({
        type: 'POST',
        url: endPoint,
        data: JSON.stringify(formData),
        contentType: 'application/json',
        xhrFields: {
            withCredentials: true
        },
        success: function(response) {
            window.location.reload();
        },
        error: function(response) {
  
            alert(response.responseJSON.Status);
        }
  
    });
  }
  
  $('#comment-form').submit((event) => {
    event.preventDefault();
    comment();
  })
});