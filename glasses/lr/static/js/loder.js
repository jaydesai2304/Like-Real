(function($) {
    "use strict";

/-- loader js --/

$("body").prepend('<div id="preloader"><div id="status">  <div class="loader"></div></div>');
$(window).on('load', function() { 
    $('#status').fadeOut();
    $('#preloader').delay(250).fadeOut('slow'); 
    $('body').delay(250).css({
        'overflow': 'visible'
    });
})
})(jQuery);
