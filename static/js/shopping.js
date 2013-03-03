/* Author: Stephen McKinney - Wojo Design */

$(function(){
    $("#demo .simpleCart_shelfItem").mouseenter(function(event) {
        $(this).find('.mytooltip').fadeIn(200);
    });
    $("#demo .simpleCart_shelfItem").mouseleave(function(event) {
        $(this).find('.mytooltip').fadeOut(200);
    });
    $("header .cartInfo").toggle(function(){
        $("#cartPopover").show();
        $("header .cartInfo").addClass('open');
    }, function(){
        $("#cartPopover").hide();
        $("header .cartInfo").removeClass('open');
    });
    
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
              x:1088,
              y:44,
              angle: 180,
              length: .2
            }
          };
        clone.appendTo('#demoShelf');
        clone.find('.mytooltip').hide();
        clone.addClass('addDemoAnimation');
        clone.css('position', 'absolute');
        clone.animate({path : new $.path.bezier(bezier_params)}, 600);
    });
    
    
    /*******************************
        Features Page
    *******************************/
    $("#btnViewAll").click(function(){
        $(this).next().slideToggle(300);
        $(this).toggleClass('active');
    });
    
    
    $("#gatewayDemoList :radio").change(function(){
        $("#gatewayDemoList .active").removeClass('active');
        $("#gatewayDemoList input:checked").parent().addClass('active');
        var newGateway = $("#gatewayDemoList input:checked").attr('id').split('-')[1];
        console.log(newGateway);
        if (newGateway === 'paypal') {
            simpleCart({
                checkout: { 
                    type: "PayPal" , 
                    email: "you@yours.com" 
                } 
            });
            
        } else if (newGateway === 'amazon') {
            simpleCart({
                checkout: { 
                    type: "AmazonPayments" , 
                    merchant_signature: "XXXXXXXXX" ,
                    merchant_id: "XXX",
                    aws_access_key_id: "XXX" ,
                    method: "GET" ,
                    sandbox: true ,
                    weight_unit: "lb" 
                } 
            });
            
        } else if (newGateway ==='google') {
            simpleCart({
                checkout: { 
                    type: "GoogleCheckout" , 
                    merchantID: "761936722557277" ,
                    method: "POST" 
                } 
            });
            
        }
        
    });
    
    $("#features-performance-visual").parent().hover(function(){
        $("#features-performance-visual #needle").addClass('moveNeedle');
    }, function(){
        $("#features-performance-visual #needle").removeClass('moveNeedle');
    });
});
