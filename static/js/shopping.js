var total_money = 0.0
var product = []
var product_count = {}
var chart_status = 0

function submit_form(event) {
    var form = $(this);
    event.preventDefault();
    if(product.length && userId)
	$.post(form.attr("action"), {"products": product.join(","), "userId": userId}, submit_callback, "json");
    return false;
}

function submit_callback(data) {
    $("#msg").html(data['result']).hide(10000);
}

$(document).ready(function(e) {
    $(".add_chart").click(function(e) {
	var target = $(e.target);
	var id = target.attr("id");
	var name = target.attr("name");
	var price = target.attr("price");
	if(!(name in product_count)) {
	    product_count[name] = 1;
	}
	else {
	    product_count[name] += 1;
	}
	count = product_count[name];
	console.log(product_count);
	total_money += parseFloat(price);
	product.push(id);
	if(!chart_status) {
	    $("#shopping_info").html("<ul><li>"+name+" * "+count+"</li></ul>");
	    chart_status = !chart_status;
	}
	else {
	    var html_str = "<ul>";
	    for(name in product_count) {
		html_str += "<li>"+name+" * "+product_count[name]+"</li>";
	    }
	    html_str += "</ul>";
	    $("#shopping_info").html(html_str);
	}
	$("#shopping_money").html("价格总计: "+total_money);
    });

    $("#submit_form").submit(submit_form);
});