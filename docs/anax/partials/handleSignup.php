<?php
$showAlert=false;
$showError=false;
if($_SERVER['REQUEST_METHOD']=='POST')
{
    include './_dbconnect.php';
    $username=$_POST['signup_username'];
    $password=$_POST['signuppassword'];
    $cpassword=$_POST['csignuppassword'];

    $existSql = "SELECT * FROM `users` WHERE user_name = '$username'";
    $result = mysqli_query($conn, $existSql);
    if($result){
    $numExistRows = mysqli_num_rows($result);
    if($numExistRows > 0){
        // $exists = true;
        $showError = "Username Already Exists";
        header("location:/php-forum-website?signup-success=false&error=$showError");
    }
    else{
        // $exists = false; 
        if(($password == $cpassword)){
            $hash = password_hash($password, PASSWORD_DEFAULT);
            $sql="INSERT INTO `users` (`user_pass`, `user_name`) VALUES ( '$hash', '$username');";
            $result = mysqli_query($conn, $sql);
            if ($result){
                $showAlert = true;
                header("location:/php-forum-website?signup-success=true");
            }
            else{
                $showError=mysqli_error($conn);
                header("location:/php-forum-website?signup-success=false&error=$showError");
            }
        }
        else{
            $showError = "Passwords do not match";
            header("location:/php-forum-website?signup-success=false&error=$showError");
        }
    }
}
else
{
    $showError=mysqli_error($conn);
    header("location:/php-forum-website?signup-success=false&error=$showError");
}
    
}
?>
