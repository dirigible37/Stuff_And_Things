<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">

<title>Winslow Mohr</title>

<!-- CSS -->
<link href="../../bootstrap/css/bootstrap.min.css" rel="stylesheet">
<link href="../../css/signin.css" rel="stylesheet">
<link href="../../css/style.css" rel="stylesheet">
<link href="../../css/homepage-style.css" rel="stylesheet">
<!-- Javascript -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script type="text/javascript" src="../../js/process_post.js"></script>

</head>

<body>

<style>

img {
	max-width:100%;
	max-height:100%;
}

.table > tbody > tr > td {
	vertical-align: middle;
}



</style>

<script type="text/javascript" src="../js/get_image.js"></script>
<script type="text/javascript">

function isDefined(x) {
	var undefined;
	return x !== undefined;
}

var url = "https://www.reddit.com/r/buildapcsales/new.json";
var items = [];
//I'm an idiot

$.getJSON(url, function(data) {
	$.each(data.data.children, function(i, post) {
		var text_style="";
		var image_name = "";
		var str = post.data.title.match(/\[(.*?)\]/)[1];
		image_name = retLinkType(str); 
		if (post.data.thumbnail == "nsfw") {
			image_name = "expired.jpg";
			text_style = "text-decoration: line-through;"
		}
		
		var price = "Unknown";
		if(post.data.title.match(/\$((?:\d|\,)*\.?\d+)/g))
			price = post.data.title.match(/\$((?:\d|\,)*\.?\d+)/g)[0];
		var image = "<img id='"+i+"_img' src='../images/"+ image_name +"' alt='"+image_name+"'></img>";
		var title = post.data.title.split(']')[1];
		var link = "<a id='"+i+"_link' class='btn btn-default' href='"+post.data.url+"' target='_blank' style='"+text_style+"'>";
		items.push( "<tr> <td class='col-md-1' rowspan=2>" + image +"</td><td id='"+i+"_price'class='col-md-1'>"+price+"</td><td class='col-md-10'>"+ link + title + "</a></td></tr>" );
		
		//Get the time post was made
		var utcseconds = post.data.created_utc;
		var d = new Date(0);
		d.setUTCSeconds(utcseconds);
		var dnow = new Date();
		var hours_since = dnow-d;
		var submit_time = "Submitted ";
		if(hours_since < 60*60*1000) {
			var mins_since = (dnow - d)/60/1000;
			submit_time = submit_time + mins_since.toFixed(0) + " minutes ago";
		}
		else {
			var hours = hours_since/60/60/1000;
			submit_time = submit_time + hours.toFixed(2) + " hours ago";
		}

		items.push("<tr><td class='col-md-1'><a id='"+i+"_perma'href='http://reddit.com/"+post.data.permalink+"' target='_blank' >Comments</a></td><td id='"+i+"_time' class='col-md-5'>"+submit_time+"</td></tr>");
});
$( "<table/>", {
	"class": "table table-striped",
	html: items.join( "" )
	}).appendTo( "body" );
});

function update_price(i, post) {
	var price = "Unknown";
	if(post.data.title.match(/\$((?:\d|\,)*\.?\d+)/g))
		price = post.data.title.match(/\$((?:\d|\,)*\.?\d+)/g)[0];
	$("#"+i+"_price").text(price);
}

function update_image(i, post) {
	var str = post.data.title.match(/\[(.*?)\]/)[1];
	var type = retLinkType(str);
	var image = "../images/"+type;
	if (post.data.thumbnail == "nsfw") {
		image = "../images/expired.jpg";
		$("#"+i+"_link").css("text-decoration", "line-through");
	}
	if(type != "")
		$("#"+i+"_img").attr("src", image);
}

function update_time(i, post) {
	var utcseconds = post.data.created_utc;
	var d = new Date(0);
	d.setUTCSeconds(utcseconds);
	var dnow = new Date();
	var hours_since = dnow-d;
	var submit_time = "Submitted ";
	if(hours_since < 60*60*1000) {
		var mins_since = (dnow - d)/60/1000;
		submit_time = submit_time + mins_since.toFixed(0) + " minutes ago";
	}
	else {
		var hours = hours_since/60/60/1000;
		submit_time = submit_time + hours.toFixed(2) + " hours ago";
	}
	$("#"+i+"_time").text(submit_time);
}

setInterval( function() {
	$.getJSON(url, function(data) {
		$.each(data.data.children, function(i, post) {
			var title = post.data.title.split(']')[1];
			$("#"+i+"_link").html(title);
			$("#"+i+"_link").attr("href", post.data.url);
			$("#"+i+"_perma").attr("href", "http://reddit.com/"+post.data.permalink);
			update_price(i, post);
			update_image(i, post);
			update_time(i, post);
		});
	});
	console.log("woot");
}, 10000);
</script>

</body>
</html>

