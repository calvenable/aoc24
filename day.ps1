$day = (Get-Date -Format "dd") # To run for a specific day, replace this with e.g. "22"
$dirName = "day$day"
$dayNumber = $day.trimStart('0')

# Create a new directory and test input file for the day
New-Item -Path "." -Name "$dirName" -ItemType "directory"
New-Item -Path "./$dirName" -Name "test.txt" -ItemType "file"

# Copy the Python template file and replace the [DAY] marker with the number of the day
Copy-Item "./template.py" -Destination "./$dirName/$dirName.py"
(Get-Content "./$dirName/$dirName.py").Replace('[DAY]', "$dirName") | Set-Content "./$dirName/$dirName.py"

# Fetch the day's input from the right URL, using my session cookie/token
$Config = Get-Content -Path "./config.json" | ConvertFrom-Json
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.Cookies.Add((New-Object System.Net.Cookie("session", $Config.sessioncookie, "/", ".adventofcode.com")))

Invoke-WebRequest -UseBasicParsing -Uri "https://adventofcode.com/2024/day/$dayNumber/input" `
-WebSession $session `
-OutFile "./$dirName/input.txt";