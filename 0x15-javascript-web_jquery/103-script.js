$(document).ready(() => {
    const fetchData = () => {
      const language = $('input#language_code').val();
      $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, (data) => {
        $('div#hello').html(data.hello);
      });
    };
    $('input#btn_translate').click(fetchData);
    $('input#language_code').keyup((evt) => {
      if (evt.keyCode === 13) fetchData();
    });
  });