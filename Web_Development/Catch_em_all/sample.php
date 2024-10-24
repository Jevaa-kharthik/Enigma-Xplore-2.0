<?php
// Generate a pseudo-random session ID
function generateSessionID() {
    return bin2hex(random_bytes(26)); // 52 characters long
}

// Set the session cookie
$session_id = generateSessionID();
setcookie('PHPSESSID', $session_id, time() + 3600, '/'); // Expires in 1 hour

echo "Generated PHPSESSID: " . $session_id;
?>
