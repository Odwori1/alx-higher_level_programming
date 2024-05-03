$(document).ready(() => {
    $('input#btn_translate').click(() => {
      const language = $('input#language_code').val();
  
      $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, (data) => {
        $('div#hello').html(data.hello);
      });
    });
  });