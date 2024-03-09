$(function () {
  // function to make api calls to events and populate the Dom with event listings
  const hostUrl = 'http://127.0.0.1:5000/api/v1/hosts'; 
  const eventUrl = 'http://127.0.0.1:5000/api/v1/events';

  // custom function to loop through event objs and add them to the dom using mustache js
  function addEvent(response, location, template, count = 0) {
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
  };

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

  // add host names to host follow tab (top-3)
  $.get(hostUrl, function (response) {
    let location = $('#follow_tab');
    let template = $('#follow_temp').html();
    addEvent(response, location, template, count=3);
  });

  // follow button event
  $('#follow_tab').on('click', '.follow_btn', function () {
    if ($(this).text() === 'follow') {
      $(this).text('followed');
    } else {
      $(this).text('follow');
  };
  });
  
});