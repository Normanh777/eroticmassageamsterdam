<?php
// One-off: copies all profile photos to this site under new names. CLI only. Safe to re-run (skips existing).
if (php_sapi_name() !== 'cli') { http_response_code(404); exit; }
@ini_set('memory_limit', '768M'); @set_time_limit(0);
$lock = fopen(__DIR__ . '/copy.lock', 'c');
if (!$lock || !flock($lock, LOCK_EX | LOCK_NB)) exit; // another run is busy
$host = 'https://escortsinschiphol.com';
function get($u) { $c = curl_init($u); curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => 1, CURLOPT_FOLLOWLOCATION => 1, CURLOPT_TIMEOUT => 60, CURLOPT_USERAGENT => 'Mozilla/5.0']); $b = curl_exec($c); $k = curl_getinfo($c, CURLINFO_HTTP_CODE); curl_close($c); return $k === 200 ? $b : false; }
$html = get("$host/escorts/Bianca/");
if (!$html) { file_put_contents(__DIR__ . '/copy.log', date('c') . " index fetch failed\n"); exit; }
preg_match_all('~/migrated/profiles/([a-z0-9-]+)/([a-z0-9-]+-\d+)\.(jpe?g|png|webp)~i', $html, $m, PREG_SET_ORDER);
$by = [];
foreach ($m as $x) { $d = strtolower($x[1]); $p = $x[0]; if (!isset($by[$d])) $by[$d] = []; if (!in_array($p, $by[$d], true)) $by[$d][] = $p; }
$dir = dirname(__DIR__) . '/images/masseuses';
if (!is_dir($dir)) mkdir($dir, 0755, true);
foreach (glob("$dir/*-erotic-massage-amsterdam.jpg") as $old) @unlink($old);      // first-version files
foreach (glob("$dir/*-erotic-massage-amsterdam-400.jpg") as $old) @unlink($old);
function save($im, $sx, $sy, $sw, $sh, $tw, $th, $file) { $d = imagecreatetruecolor($tw, $th); imagefill($d, 0, 0, imagecolorallocate($d, 23, 18, 26)); imagecopyresampled($d, $im, 0, 0, $sx, $sy, $tw, $th, $sw, $sh); imageinterlace($d, true); imagejpeg($d, $file, 82); imagedestroy($d); }
$man = []; $err = [];
foreach ($by as $slug => $paths) {
  $n = 0;
  foreach ($paths as $p) {
    $i = $n + 1; $base = "$dir/$slug-erotic-massage-amsterdam";
    if (is_file("$base-$i.jpg") && is_file("$base-$i-400.jpg") && ($i > 1 || is_file("$base-card-400.jpg"))) { $n++; continue; }
    $bin = get($host . $p);
    $im = $bin ? @imagecreatefromstring($bin) : false;
    if (!$im) { $err[] = "$p " . ($bin ? 'decode' : 'download'); continue; }
    $w = imagesx($im); $h = imagesy($im);
    if ($i === 1) { // 4:5 card crop, slightly towards the top
      $cw = $w; $chh = (int) round($w * 1.25); if ($chh > $h) { $chh = $h; $cw = (int) round($h * 0.8); }
      $x = (int) (($w - $cw) / 2); $y = (int) (($h - $chh) / 4);
      save($im, $x, $y, $cw, $chh, 800, 1000, "$base-card.jpg");
      save($im, $x, $y, $cw, $chh, 400, 500, "$base-card-400.jpg");
    }
    $s = min(1, 1100 / max($w, $h)); save($im, 0, 0, $w, $h, max(1, (int) round($w * $s)), max(1, (int) round($h * $s)), "$base-$i.jpg");
    $s = min(1, 400 / $w); save($im, 0, 0, $w, $h, max(1, (int) round($w * $s)), max(1, (int) round($h * $s)), "$base-$i-400.jpg");
    imagedestroy($im); $n++;
    file_put_contents(__DIR__ . '/copy.log', date('c') . " working: $slug $i\n");
  }
  $man[] = "$slug:$n";
}
file_put_contents(__DIR__ . '/copy.log', date('c') . " DONE\n" . implode(' ', $man) . "\nerrors: " . (implode('; ', $err) ?: 'none') . "\n");
