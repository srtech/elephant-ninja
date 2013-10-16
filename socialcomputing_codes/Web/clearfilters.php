<?php
function clearFilters() {
	$c = $_POST['clear'];
	if ($c == 1)
		file_put_contents("filters.txt", "");	
}
clearFilters();
echo "Cleared!" . PHP_EOL;
?>