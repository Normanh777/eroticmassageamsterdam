<?php
// One-off: copies the masseuse portraits to this site under new names. CLI only.
if (php_sapi_name() !== 'cli') { http_response_code(404); exit; }
$base = 'https://passionescorts.nl/hcgi/platform/api/files/escorts/';
$src = [
 'vicky' => '5zdh8dbzwmex0kw/passion-vicky-db68a2-portrait.jpg',
 'bianca' => 'sdvztk16s5o6l0r/passion-bianca-f45a40-portrait.jpg',
 'sophie' => '85awomlst4ejq3y/passion-sophie-a1b2c3-portrait.jpg',
 'alexandra' => 'tbhtbekky6tl8bx/passion-alexandra-2f3a4b-portrait.jpg',
 'olga' => 'cphrzxcuvf12746/passion-olga-775c70-portrait.webp',
 'lavinia' => 'ynbt57p03d9uyvm/passion-lavinia-96eb0b-portrait.webp',
 'miki' => '3scycfdf9pr9vce/passion-miki-a5c6cc-portrait.jpg',
 'alessia' => 'ey90r8h6zik1l2v/passion-alessia-0b1c2d-portrait.webp',
 'brianna' => 'y62tw0wsgcgj12w/passion-brianna-7c9723-portrait.jpeg',
];
$dir = dirname(__DIR__) . '/images/masseuses';
if (!is_dir($dir)) mkdir($dir, 0755, true);
$log = [];
foreach ($src as $slug => $path) {
  $out = "$dir/$slug-erotic-massage-amsterdam";
  if (is_file("$out.jpg") && is_file("$out-400.jpg")) { $log[] = "$slug: exists"; continue; }
  $ch = curl_init($base . $path);
  curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 40, CURLOPT_USERAGENT => 'Mozilla/5.0']);
  $bin = curl_exec($ch); $code = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
  if ($code !== 200 || !$bin) { $log[] = "$slug: download failed ($code)"; continue; }
  $im = function_exists('imagecreatefromstring') ? @imagecreatefromstring($bin) : false;
  if (!$im) { $log[] = "$slug: cannot decode (" . strlen($bin) . " bytes)"; continue; }
  $w = imagesx($im); $h = imagesy($im);
  $cw = $w; $ch2 = (int) round($w * 5 / 4);
  if ($ch2 > $h) { $ch2 = $h; $cw = (int) round($h * 4 / 5); }
  $x = (int) (($w - $cw) / 2); $y = (int) (($h - $ch2) / 4); // crop slightly towards the top
  foreach ([[800, 1000, ''], [400, 500, '-400']] as [$tw, $th, $suf]) {
    $dst = imagecreatetruecolor($tw, $th);
    imagecopyresampled($dst, $im, 0, 0, $x, $y, $tw, $th, $cw, $ch2);
    imageinterlace($dst, true);
    imagejpeg($dst, "$out$suf.jpg", 82);
    imagedestroy($dst);
  }
  imagedestroy($im);
  $log[] = "$slug: ok {$w}x{$h} -> " . filesize("$out.jpg") . " / " . filesize("$out-400.jpg") . " bytes";
}
file_put_contents(__DIR__ . '/fetch.log', date('c') . "\n" . implode("\n", $log) . "\n");
