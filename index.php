<?php

$command = escapeshellcmd('python paramikotestmousemultiple2.py');

$output = shell_exec($command);
echo $output;

?>
