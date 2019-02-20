<?php
require_once 'header.php';

$op = isset($_REQUEST['op']) ? my_filter($_REQUEST['op'], "string") : '';

switch ($op) {
    case 'index':
        index_list();
        break;
    
    default:
        # code...
        break;
}

// function

function index_list() {
    global $mysqli;
    $sql = "SELECT * FROM `class` ORDER BY `class_sn` DESC";
    $result = $mysqli->query($sql) or die($mysqli->connect_error);
    $i = 0;
    while ($class = $result->fetch_assoc()) {
        if ($class['class_display'] == 'enable') {
            $all_class[$i] = $class;
            $i ++;
        }
    }
    echo $all_class;
}