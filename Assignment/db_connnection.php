<?php
function OpenCon()
 {
 $dbhost = "localhost";
 $dbuser = "taibat";
 $dbpass = "Omolol@1992";
 $db = "practice";
 $conn = new mysqli($dbhost, $dbuser, $dbpass,$db) or die("Connect failed: %s\n". $conn -> error);
 
 return $conn;
 }
 
function CloseCon($conn)
 {
 $conn -> close();
 }
   
?>