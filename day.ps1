$dirName = "day" + (Get-Date -Format "dd")

New-Item -Path "." -Name "$dirName" -ItemType "directory"
New-Item -Path "./$dirName" -Name "test.txt" -ItemType "file"
New-Item -Path "./$dirName" -Name "input.txt" -ItemType "file"

Copy-Item "./template.py" -Destination "./$dirName/$dirName.py"
(Get-Content "./$dirName/$dirName.py").Replace('[DAY]', "$dirName") | Set-Content "./$dirName/$dirName.py"
