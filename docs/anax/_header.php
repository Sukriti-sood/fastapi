<?php
session_start();
$logedin=false;
if($_SESSION['loggedin']&&$_SESSION['loggedin']==true)
{
  $logedin=true;
}
echo ' <nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
<div class="container-fluid">
  <a class="navbar-brand" href="./">phpForum</a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
  
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="./">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="./about.php">About</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
          Categories
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
          <li><a class="dropdown-item" href="#">Action</a></li>
          <li><a class="dropdown-item" href="#">Another Action</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#">Something else here</a></li>
        </ul>
      </li>
      <li class="nav-item">
        <a class="nav-link " href="./contact.php" tabindex="-1" >Contact</a>
      </li>
    </ul>
    
    <form class="d-flex">
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-success" type="submit">Search</button>
    </form>';
    if($logedin)
    {
      $user_name=$_SESSION['user_name'];
      echo '<p class="text-light mx-2 my-0">Welcome '.$user_name.'</p>
      <button class="btn btn-outline-success" type="submit"><a class="text-light" href="./partials/logout.php">Logout</a></button>
      ';
    }
    else{
      echo '
      <button class="btn btn-outline-success mx-2" type="submit" data-bs-toggle="modal" data-bs-target="#loginModal">Login</button>
    <button class="btn btn-outline-success" type="submit" data-bs-toggle="modal" data-bs-target="#signupModal">Signup</button>
     ';
    }
  echo '</div>
</div>
</nav>
';

include './partials/_signupmodal.php';

include './partials/_loginmodal.php';

?>
