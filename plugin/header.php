<?php
define('_DB_HOST', '210.70.138.227');
define('_DB_ID', 'root');
define('_DB_PW', 'tfcis.test');
define('_DB_NAME', 'arashi');

$mysqli = new mysqli(_DB_HOST, _DB_ID, _DB_PW, _DB_NAME);

if ($mysqli->connect_error) {
    die('無法連上資料庫 (' . $mysqli->connect_errno . ') '
        . $mysqli->connect_error);
}