<?php
/******************************************************************************
* EEGLAB form handler, safer PHP 5 compatible rewrite
******************************************************************************/

/* Temporary debugging. Remove or disable after testing. */
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

/* Configuration */
$MESSAGE_FILE = '/var/local/eeglab/eeglablog.txt'; /* keep outside web root */
$DEFAULT_EXIT_PAGE = 'https://eeglab.org/others/Download_Success.html';
$ERROR_EMAIL = 'arno@ucsd.edu';
$REPLY_TO_EMAIL = 'arno@ucsd.edu';

/* Helpers */

function send_error_email($subject, $details, $fromEmail, $errorEmail, $replyToEmail)
{
    $safeFromEmail = filter_var($fromEmail, FILTER_VALIDATE_EMAIL) ? $fromEmail : $replyToEmail;

    $headers = 'From: <' . $safeFromEmail . '>' . "\r\n" .
               'Reply-To: ' . $replyToEmail . "\r\n" .
               'MIME-Version: 1.0' . "\r\n" .
               'Content-Type: text/plain; charset=UTF-8' . "\r\n" .
               'Content-Transfer-Encoding: 8bit' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    @mail($errorEmail, $subject, $details, $headers);
}

function fail_and_email($publicMessage, $internalMessage, $fromEmail, $errorEmail, $replyToEmail)
{
    send_error_email('eeglab.php error', $internalMessage, $fromEmail, $errorEmail, $replyToEmail);
    header('Content-Type: text/plain; charset=UTF-8');
    echo $publicMessage;
    exit;
}

function sanitize_header_value($value)
{
    $value = trim((string)$value);
    $value = str_replace("\r", '', $value);
    $value = str_replace("\n", '', $value);
    return $value;
}

function normalize_post_value($value)
{
    if (is_array($value)) {
        $parts = array();
        foreach ($value as $item) {
            $parts[] = normalize_post_value($item);
        }
        return implode(', ', $parts);
    }
    return trim((string)$value);
}
/* Only accept POST */
if (!isset($_SERVER['REQUEST_METHOD']) || $_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('HTTP/1.1 405 Method Not Allowed');
    header('Allow: POST');
    header('Content-Type: text/plain; charset=UTF-8');
    echo 'Method not allowed';
    exit;
}

/* Read known fields only */
$username = isset($_POST['username']) ? sanitize_header_value(normalize_post_value($_POST['username'])) : '';
$emailRaw = isset($_POST['email']) ? sanitize_header_value(normalize_post_value($_POST['email'])) : '';
$email = filter_var($emailRaw, FILTER_VALIDATE_EMAIL) ? $emailRaw : '';

$eegnews = isset($_POST['eeglabnews']) ? 1 : 0;
$eeglist = isset($_POST['eeglablist']) ? 1 : 0;

/* Build plain text log entry */
$timestamp = date('c');
$remoteAddr = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '';
$userAgent = isset($_SERVER['HTTP_USER_AGENT']) ? $_SERVER['HTTP_USER_AGENT'] : '';
$referer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '';

$logLines = array();
$logLines[] = 'date: ' . $timestamp;
$logLines[] = 'ip: ' . $remoteAddr;
$logLines[] = 'user_agent: ' . $userAgent;
$logLines[] = 'referer: ' . $referer;

foreach ($_POST as $key => $val) {
    $safeKey = preg_replace('/[^a-zA-Z0-9_.-]/', '_', (string)$key);
    $safeVal = normalize_post_value($val);
    $logLines[] = $safeKey . ': ' . $safeVal;
}

$logLines[] = str_repeat('=', 60);
$logEntry = implode("\n", $logLines) . "\n";

/* Check directory exists */
$dir = dirname($MESSAGE_FILE);
if (!is_dir($dir)) {
    fail_and_email(
        'Server error',
        'Log directory does not exist: ' . $dir,
        $email,
        $ERROR_EMAIL,
        $REPLY_TO_EMAIL
    );
}

/* Append safely to log */
$fp = fopen($MESSAGE_FILE, 'ab');
if ($fp === false) {
    fail_and_email(
        'Server error',
        'Could not open log file for append: ' . $MESSAGE_FILE,
        $email,
        $ERROR_EMAIL,
        $REPLY_TO_EMAIL
    );
}

if (!flock($fp, LOCK_EX)) {
    fclose($fp);
    fail_and_email(
        'Server error',
        'Could not lock log file: ' . $MESSAGE_FILE,
        $email,
        $ERROR_EMAIL,
        $REPLY_TO_EMAIL
    );
}

$bytesWritten = fwrite($fp, $logEntry);
fflush($fp);
flock($fp, LOCK_UN);
fclose($fp);

if ($bytesWritten === false) {
    fail_and_email(
        'Server error',
        'Could not write to log file: ' . $MESSAGE_FILE,
        $email,
        $ERROR_EMAIL,
        $REPLY_TO_EMAIL
    );
}

/* Tighten permissions if possible */
if (file_exists($MESSAGE_FILE)) {
    @chmod($MESSAGE_FILE, 0640);
}

/* Optional mailing list subscriptions */
if ($email !== '') {
    $displayName = ($username !== '') ? $username : 'EEGLAB user';
    $displayName = str_replace('"', '\\"', $displayName);

    $headers = 'From: "' . $displayName . '" <' . $email . '>' . "\r\n" .
               'Reply-To: ' . $email . "\r\n" .
               'MIME-Version: 1.0' . "\r\n" .
               'Content-Type: text/plain; charset=UTF-8' . "\r\n" .
               'Content-Transfer-Encoding: 8bit' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    if ($eegnews) {
        if (!@mail('eeglabnews-subscribe@sccn.ucsd.edu', 'Subscribe eeglabnews', '', $headers)) {
            send_error_email(
                'eeglab.php error',
                'Failed to send eeglabnews subscription email for: ' . $email,
                $email,
                $ERROR_EMAIL,
                $REPLY_TO_EMAIL
            );
        }
    }

    if ($eeglist) {
        if (!@mail('eeglablist-subscribe@sccn.ucsd.edu', 'Subscribe eeglablist', '', $headers)) {
            send_error_email(
                'eeglab.php error',
                'Failed to send eeglablist subscription email for: ' . $email,
                $email,
                $ERROR_EMAIL,
                $REPLY_TO_EMAIL
            );
        }
    }
}

/* Redirect on success */
header('Location: ' . $DEFAULT_EXIT_PAGE, true, 303);
exit;

?>
                                                                                                                            192,1         Bot
