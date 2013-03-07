simpleCart.currency({
    code: "CNY" ,
    name: "Chinese Yuan" ,
    symbol: "¥" ,
    delimiter: " " , 
    decimal: "." , 
    after: true ,
    accuracy: 2
});
simpleCart({
    cartColumns: [
	{ view: function(item, column){
	    return  "<span>"+item.get('quantity')+"</span>" + 
		"<div>" +
		"<a href='javascript:;' class='simpleCart_increment'><img src='/static/img/increment.png' title='+1' alt='arrow up'/></a>" +
		"<a href='javascript:;' class='simpleCart_decrement'><img src='/static/img/decrement.png' title='-1' alt='arrow down'/></a>" +
		"</div>";
	}, attr: 'custom' },
	{ attr: "name", label: false },
	{ view: "currency", attr: "total", label: "小项合计" },
    ],
    cartStyle: "div",
    checkout: { 
        type: "SendForm" ,
        url: "/checkout/",
        method: "POST"
    }
});