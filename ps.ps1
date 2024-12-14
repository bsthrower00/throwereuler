# Change this path to the directory you want to open PowerShell in
$directoryPath = "C:\Users\nobutty\Documents\ProjE"

# Change the title of the PowerShell window as desired
$title = "My Custom PowerShell"

# Open PowerShell in the specified directory
Start-Process -WorkingDirectory $directoryPath -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "cd '$directoryPath'", "-WindowTitle '$title'" -WindowStyle Maximized
