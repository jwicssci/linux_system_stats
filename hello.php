<?php 
	chdir('/usr/lib/cgi-bin');
	$output = shell_exec('./stats.cgi');
	$stats = str_replace("Content-type: text/html", "", $output);
	echo "<p>$stats</p>";
?>

