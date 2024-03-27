function loadHostNames(req_url) {
  // add host names to host follow tab (top-3)
  $.ajax({
    url: 'follow_template.html',
    dataType: 'html',
    success: function(hostTemplate) {
      $.ajax({
        type: 'GET',
        url: req_url,
        xhrFields: {
          withCredentials: true
        },
        success: function(response) {
          let location = $('#follow_tab');
          addEvent(response, location, hostTemplate, count=3);
        }
      });
    }
  });
}


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


$(document).ready(function () {
  // function to make api calls to events and populate the Dom with event listings
  let userId = localStorage.getItem('user_id');
  let hostUrl;
  // check if user is sign in and return hosts user is not following
  // else return the unsorted host list
  if (userId === null) {
    hostUrl = `http://127.0.0.1:5000/api/v1/hosts`;
  } else {
    hostUrl = `http://127.0.0.1:5000/api/v1/users/${userId}/notfollowings`;
  }

  const eventUrl = 'http://127.0.0.1:5000/api/v1/events';
  
  // add event listing to home tab
  $.get(eventUrl, function (response) {
    let location = $('#home');
    let template = $('#mytemp').html();
    addEvent(response, location, template);
  });

  // add event names to popular tab (top-3)
  $.get(eventUrl, function (response) {
    let location = $('#eventlist');
    let template = $('#sidebar_temp').html();
    addEvent(response, location, template, count=3);
  });
  
  loadHostNames(hostUrl);
  
  // follow button event
  $('#follow_tab').on('click', '.follow_btn', function () {
    if (userId === null) {
      alert('Sign in with a User account to follow Host. Don\'t have an account? Pls sign up')
      return;
    }
    const postUrl = `http://127.0.0.1:5000/api/v1/users/${userId}/followings`;
    const requestData = {
      host_id: $(this).data('host-id')
  };
    $.ajax({
      type: 'POST',
      url: postUrl,
      xhrFields: {
        withCredentials: true
      },
      data: JSON.stringify(requestData),
      contentType: 'application/json',
      success: function(response) {
        $('#follow_tab').text('');
        loadHostNames(hostUrl);
      },
      error: function(textStatus, errorThrown) {
        console.error('AJAX error:', textStatus, errorThrown);
        window.location.href = 'sign-in.html';
      }
    });
  });
});