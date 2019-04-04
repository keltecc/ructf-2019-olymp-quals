<?php

function dump_config($settings) {
    unset($_SESSION["config"]);
    $params = [];
    
    array_walk(
        array_merge($settings, $_SESSION), 
        function ($value, $key) use (&$params) {
            $params[] = "$key=$value";
    });

    $config = implode("\n", $params);
    $filename = "./files/".sha1($config);
    file_put_contents($filename, $config);

    $_SESSION["config"] = $filename;
}

function read_config() {
    $config = file_get_contents($_SESSION["config"]);
    $params = [];

    array_walk(
        explode("\n", $config),
        function ($value, $key) use (&$params) {
            $parts = explode("=", $value);
            $params[$parts[0]] = $parts[1];
    });
    
    return $params;
}

session_start();

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    switch ($_GET["action"]) {
        case "login":
            if (isset($_SESSION["username"])) {
                $_SESSION["message"] = "You have already logged in!";
                break;
            }
            $_SESSION["username"] = $_POST["username"];
            $_SESSION["is_admin"] = 0;
            dump_config([
                "city" => "unknown",
                "gender" => "not selected"
            ]);
            break;
        
        case "logout":
            if (!isset($_SESSION["username"])) {
                $_SESSION["message"] = "You need to login first!";
                break;
            }
            unlink($_SESSION["config"]);
            session_destroy();
            break;

        case "profile":
            if (!isset($_SESSION["username"])) {
                $_SESSION["message"] = "You need to login first!";
                break;
            }
            dump_config($_POST);
            $_SESSION["message"] = "Your settings was updated succesfully.";
            break;

        case "vote":
            // TODO: implement saving the vote
            $_SESSION["message"] = "Thank you for the vote!";
            break;
    }

    header("Location: /");
    exit();
}

if (!isset($_SESSION["username"]) && (!isset($_GET["action"]) || $_GET["action"] !== "login"))
    header("Location: /?action=login");

?>
<!DOCTYPE html>
<html>
    <head>
        <title>Voting System</title>
        <link rel="stylesheet" href="/files/styles.css">
    </head>
    <body>
        <div class="head">
            <a href="/" class="titl">Voting system</a>
<?php 

if (isset($_SESSION["username"]))
    echo "            <span class=\"usrn\">(".$_SESSION["username"].")</span>\n"; 

?>
        </div>
        <div class="main">
<?php

if (isset($_SESSION["message"])) {
    echo "            <h1 class=\"eror\">".$_SESSION["message"]."</h1>\n";
    unset($_SESSION["message"]);
}

$user_config = read_config();

switch ($_GET["action"]) {
    case "login":

?>
            <h1>Login:</h1>
            <form method="post" action="/?action=login">
                <input type="text" name="username" placeholder="username">
                <input type="submit" value="Login">
            </form>
<?php

        break;
    case "vote":

?>
            <h1>Vote here!</h1>
            <form method="post" action="/?action=vote">
                <input type="text" name="score" placeholder="5">
                <input type="submit" value="Vote">
            </form>
<?php
        break;
    case "profile":

?>
            <h1>Account settings:</h1>
            <img src="https://thispersondoesnotexist.com/image" >
            <form method="post" action="/?action=profile">
<?php

    foreach ($user_config as $key => $value) {
        if ($key == "username" || $key == "is_admin")
            continue;
        echo "                <label for=\"$key\">$key</label>\n";
        echo "                <input type=\"text\" id=\"$key\" name=\"$key\" value=\"$value\"><br>\n";
    }

?>
                <input type="submit" value="Update">
            </form>
<?php

        break;
    case "admin":
        if (!isset($user_config["is_admin"]) || $user_config["is_admin"] != 1) {
            echo "            <h1>Sorry, you are not admin!</h1>\n";
        }
        else {
            $flag = file_get_contents("flag.txt");
            echo "            <h1>Admin panel:</h1>\n";
            echo "            <h1>$flag</h1>\n";
        }
        break;
    default:

?>
            <h1>Main menu:</h1>
            <a href="/?action=vote">Vote</a><br>
            <a href="/?action=profile">Profile</a><br>
            <a href="/?action=admin">Admin panel</a><br>
            <form method="post" action="/?action=logout">
                <input type="submit" value="Logout">
            </form>
<?php

        break;
}

?>
        <!-- sorry for the design -->
    </body>
</html>
