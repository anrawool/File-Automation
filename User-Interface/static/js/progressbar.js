$(document).ready(function() {
    // Get the file upload form element
    var form = $('#upload-form');
  
    // Bind the submit event
    form.on('submit', function(event) {
      event.preventDefault();
  
      // Create a FormData object to handle the file upload
      var formData = new FormData(this);
  
      // Create an Ajax request to handle the file upload
      $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: formData,
        processData: false,
        contentType: false,
        xhr: function() {
          // Create an XHR object to track the upload progress
          var xhr = new window.XMLHttpRequest();
  
          // Attach an event listener to the XHR object to track the progress
          xhr.upload.addEventListener('progress', function(event) {
            if (event.lengthComputable) {
              // Calculate the upload progress percentage
              var percent = (event.loaded / event.total) * 100;
  
              // Update the progress bar width based on the progress percentage
              $('#progress-bar-fill').css('width', percent + '%');
            }
          }, false);
  
          return xhr;
        },
        success: function(response) {
          // Handle the success response after the file upload is complete
          console.log(response);
        },
        error: function(xhr, status, error) {
          // Handle the error response
          console.error(error);
        }
      });
    });
  });
  