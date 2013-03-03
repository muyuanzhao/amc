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
            position = $(this).position();
        clone.appendTo('#demoShelf');
        clone.find('.mytooltip').hide();
        clone.addClass('addDemoAnimation');
        clone.removeClass('span2');
        clone.css('position', 'absolute');
        clone.animate({
            crSpline: $.crSpline.buildSequence([[position.left, position.top], [2400-position.left, 200-position.top]]),
            duration: 600,
            width:"0px"
        });
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
