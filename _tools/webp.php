<?php
// One-off: create a .webp next to every .jpg in images/masseuses. Deletes and overwrites nothing. CLI only.
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
set_time_limit(0);
$root = dirname(__DIR__);
$log = __DIR__ . '/webp-log.txt';
if (file_exists(__DIR__ . '/webp.done')) { exit; }
if (file_exists(__DIR__ . '/webp.lock') && time() - filemtime(__DIR__ . '/webp.lock') < 900) { exit; }
touch(__DIR__ . '/webp.lock');
if (!function_exists('imagewebp') || !function_exists('imagecreatefromjpeg')) {
    file_put_contents($log, "ERROR: GD with WebP support is not available (PHP " . PHP_VERSION . ")\n");
    touch(__DIR__ . '/webp.done'); unlink(__DIR__ . '/webp.lock'); exit;
}
$made = 0; $skip = 0; $fail = 0; $jb = 0; $wb = 0; $bigger = 0;
foreach (glob($root . '/images/masseuses/*.jpg') as $jpg) {
    $webp = substr($jpg, 0, -4) . '.webp';
    if (file_exists($webp) && filesize($webp) > 0) { $skip++; $jb += filesize($jpg); $wb += filesize($webp); continue; }
    $im = @imagecreatefromjpeg($jpg);
    if (!$im) { $fail++; continue; }
    $ok = @imagewebp($im, $webp, 80);
    imagedestroy($im);
    if (!$ok || !file_exists($webp) || filesize($webp) === 0) { @unlink($webp); $fail++; continue; }
    if (filesize($webp) % 2 === 1) { file_put_contents($webp, "\0", FILE_APPEND); }
    $made++; $jb += filesize($jpg); $wb += filesize($webp);
    if (filesize($webp) >= filesize($jpg)) { $bigger++; }
}
file_put_contents($log, sprintf("made=%d skipped=%d failed=%d bigger=%d jpg_kb=%d webp_kb=%d php=%s\n", $made, $skip, $fail, $bigger, $jb / 1024, $wb / 1024, PHP_VERSION));
touch(__DIR__ . '/webp.done'); unlink(__DIR__ . '/webp.lock');
