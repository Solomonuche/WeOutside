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
});