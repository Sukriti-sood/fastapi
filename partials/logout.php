 
<?php

if($_SESSION['loggedin'] = true)
{
    session_start();
    session_unset();
    session_destroy();
    header("location: /php-forum-website");
}


?>
