<?php 
passthru('/etc/motion/motionjour.sh');
sleep(1);
header('Location: index.html');
?>

