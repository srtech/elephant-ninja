<?php
function saveFilter() {
	$res['from'] = $_POST['from'];
	$res['to'] = $_POST['to'];
	$res['subject'] = $_POST['subject'];
	$res['hasw'] = $_POST['hasw'];
	$res['hasnotw'] = $_POST['hasnotw'];
	$res['rsptext'] = $_POST['rsptext'];
	
	$jsonres = json_encode($res);
	
	$fp = fopen("filters.txt", 'a');
	fwrite($fp, $jsonres . PHP_EOL);
	fclose($fp);
}

saveFilter();

echo "done" . PHP_EOL;
?>