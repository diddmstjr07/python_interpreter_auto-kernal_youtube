$dir = (Get-Location).Path
$url = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
$output = Join-Path -Path $dir -ChildPath "python-3.10.0-amd64.exe"

Invoke-WebRequest -Uri $url -OutFile $output

Start-Process -FilePath $output -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Verb RunAs -Wait

python --version
