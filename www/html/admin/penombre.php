<?php 
passthru('/etc/motion/motionmoy.sh');
sleep(1);
header('Location: index.html');
?>

