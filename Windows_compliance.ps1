# Windows Endpoint Compliance Checker
# Checks Windows Firewall, Antivirus, BitLocker, and Update status

$report = @{
    Hostname = $env:COMPUTERNAME
    DateTime = (Get-Date).ToString("s")
}

# Check Firewall
$firewallStatus = Get-NetFirewallProfile | Select-Object Name, Enabled
$report["Firewall"] = $firewallStatus

# Check Antivirus (Defender)
$avStatus = Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled
$report["Antivirus"] = $avStatus

# Check BitLocker Encryption (only for C:)
$bitlocker = Get-BitLockerVolume -MountPoint "C:" | Select-Object VolumeStatus, ProtectionStatus
$report["BitLocker"] = $bitlocker

# Check Last Installed Update
$lastUpdate = Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 1
$report["LastUpdate"] = $lastUpdate.InstalledOn

# Save report as JSON
$report | ConvertTo-Json -Depth 5 | Out-File "$env:USERPROFILE\Desktop\compliance_report_win.json"
