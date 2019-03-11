<?php 
passthru('/home/pi/www/html/admin/stopcamera.py');
sleep(1);
header('Location: index.html');
exit;
?>

