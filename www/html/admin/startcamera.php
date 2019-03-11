<?php 
passthru('/home/pi/www/html/admin/startcamera.py');
sleep(1);
header('Location: index.html');
exit;
?>

