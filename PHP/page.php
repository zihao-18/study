<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>Examples</title>
<meta name="description" content="">
<meta name="keywords" content="">
<link href="" rel="stylesheet">
</head>
<body>
	<div>
		
		<?php
			$arre = array();
			$arr['123'] = array("username"=>"张三","chinese"=>"130","math"=>"140","english"=>"150","summary"=>"298");
			$arr['124'] = array("username"=>"李四","chinese"=>"110","math"=>"120","english"=>"130","summary"=>"248");
			$arr['125'] = array("username"=>"王五","chinese"=>"100","math"=>"123","english"=>"130","summary"=>"218");
			$arr['126'] = array("username"=>"赵六","chinese"=>"130","math"=>"140","english"=>"150","summary"=>"238");

			$code = $_POST['code'];

			$score = $arr[$code];
		?>
	</div>
    
</body>
</html>