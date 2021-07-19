$(document).ready(function(){
  $('#rateforms').submit(function(event){
    event.preventDefault();
    form = $('#rateforms')
    $.ajax({
      'url': '/ajax/ratereview/', // link
      'type': 'POST', // method 
      'data': form.serialize(), // turns from data to json
      'dataType':'json', // the data type
      'success': function(data){
        alert(data['success'])
        $('#id_design').val('');
        $('#id_usability').val('');
        $('#id_content').val('');
        $('#id_review').val('');
      }
    })
  })

  $('[data-toggle="tooltip"]').tooltip(); 
})