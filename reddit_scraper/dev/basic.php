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

<script type="text/javascript">

function isDefined(x) {
	var undefined;
	return x !== undefined;
}

var url = "https://www.reddit.com/r/buildapcsales/new.json";
var items = [];

$.getJSON(url, function(data) {
	$.each(data.data.children, function(i, post) {
		var text_style="";
		if (post.data.thumbnail == "nsfw") {
			text_style = "text-decoration: line-through;"
		}
		
		var link = "<a id='"+i+"_link' class='btn btn-default' href='"+post.data.url+"' target='_blank' style='"+text_style+"'>";
		items.push( "<tr><td class='col-md-10'>"+ link + post.data.title + "</a></td></tr>" );
});
$( "<table/>", {
	"class": "table table-striped",
	html: items.join( "" )
	}).appendTo( "body" );
});
</script>

</body>
</html>

