<?php
    if(isset($_GET['signup-success']) && $_GET['signup-success']=="true"){
        echo '
        <div class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Holy guacamole!</strong> You can login 🎉.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        
        ';
      }
      elseif(isset($_GET['error'])&&$_GET['error'])
      {
        $error=$_GET['error'];
        echo '
               
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Holy guacamole!</strong>'.$error.'
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        
        ';
      }
      elseif(isset($_GET['login-success'])&&$_GET['login-success']=="true")
      {
        echo '
               
        <div class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Welcome!</strong> You are Logged in 🎉.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        
        ';
      }
      elseif(isset($_GET['lerror'])&&$_GET['lerror'])
      {
        $error=$_GET['lerror'];
        echo '
               
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Holy guacamole!</strong>'.$error.'
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        
        ';
      }       
?>   
        
