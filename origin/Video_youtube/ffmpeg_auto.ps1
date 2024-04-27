$url_ffmpeg = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
$output_ffmpeg = "C:\ffmpeg-release-essentials.zip"
Invoke-WebRequest -Uri $url_ffmpeg -OutFile $output_ffmpeg
$extractPath_ffmpeg = "C:\"
Expand-Archive -Path $output_ffmpeg -DestinationPath $extractPath_ffmpeg -Force
$dirPath = "C:\ffmpeg-6.1.1-essentials_build\bin"
$path = [Environment]::GetEnvironmentVariable("PATH", "Machine")

if ($path -notlike "*$dirPath*") {
    $path += ";$dirPath"
}

[Environment]::SetEnvironmentVariable("PATH", $path, "Machine")

