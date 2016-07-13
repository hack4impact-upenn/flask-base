// Semantic UI breakpoints
var mobileBreakpoint = '768px';
var tabletBreakpoint = '992px';
var smallMonitorBreakpoint = '1200px';

$(document).ready(function () {

    // Enable dismissable flash messages
    $('.message .close').on('click', function () {
        $(this).closest('.message').transition('fade');
    });

    // Enable mobile navigation
    $('#open-nav').on('click', function () {
        $('.mobile.only .vertical.menu').transition('slide down');
    });

    // Enable sortable tables
    $('table.ui.sortable').tablesort();

    // Enable dropdowns
    $('.dropdown').dropdown();
    $('select').dropdown();

    // mobile dropdown
    
});


// Add a case-insensitive version of jQuery :contains pseduo
// Used in table filtering
(function ($) {
    function icontains(elem, text) {
        return (elem.textContent || elem.innerText || $(elem).text() || "")
                .toLowerCase().indexOf((text || "").toLowerCase()) > -1;
    }

    $.expr[':'].icontains = $.expr.createPseudo ?
        $.expr.createPseudo(function (text) {
            return function (elem) {
                return icontains(elem, text);
            };
        }) :
        function (elem, i, match) {
            return icontains(elem, match[3]);
        };
})(jQuery);
 // mobile dropdown menu state change 
  var currentState = []
  function changeMenu(e) {
    var children = $($(e).children()[1]).html();
    currentState.push($('.mobile.only .vertical.menu').html());
    children += '<a class="item" onClick="back()">Back</a><i class="back icon"></i>'
    $('.mobile.only .vertical.menu').html(children);
  }
  function back() {
    $('.mobile.only .vertical.menu').html(currentState.pop());
  }
