$("#demo .simpleCart_shelfItem").mouseenter(function(event) {
    $(this).find('.tooltip').fadeIn(200);
});
$("#demo .simpleCart_shelfItem").mouseleave(function(event) {
    $(this).find('.tooltip').fadeOut(200);
});

$("header .cartInfo").toggle(function(){
    $("#cartPopover").show();
    $("header .cartInfo").addClass('open');
}, function(){
    $("#cartPopover").hide();
    $("header .cartInfo").removeClass('open');
});


$("#demoShelf .simpleCart_shelfItem:eq(0)").css('left', '310px');
$("#demoShelf .simpleCart_shelfItem:eq(1)").css('left', '171px');
$("#demoShelf .simpleCart_shelfItem:eq(2)").css('left', '29px');
$("#demoShelf .simpleCart_shelfItem").delay(500).animateStep({css:{top:'0px'},delay:100,speed:100});
$("#demoShelf .simpleCart_shelfItem").click(function(){
    $(".intro").css('overflow','visible');
    var clone = $(this).clone(),
        position = $(this).position(),
        bezier_params = {
        start: { 
          x: position.left, 
          y: 0, 
          angle: -90
        },  
        end: { 
          x:310,
          y:-210, 
          angle: 180, 
          length: .2
        }
      };

    clone.appendTo('#demoShelf');
    clone.find('.tooltip').hide();
    clone.addClass('addDemoAnimation');
    clone.animate({path : new $.path.bezier(bezier_params)}, 600);
});

