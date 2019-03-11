<?php 
passthru('/etc/motion/motionnuit.sh');
sleep(1);
header('Location: index.html');
?>

