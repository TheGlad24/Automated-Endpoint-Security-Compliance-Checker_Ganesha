# Updated macOS Endpoint Compliance Checker
# Save as check_compliance_macos.py

import subprocess, json
from datetime import datetime

report = {
    "hostname": subprocess.getoutput("scutil --get ComputerName"),
    "datetime": datetime.now().isoformat()
}

# Check Firewall status
report["Firewall"] = subprocess.getoutput("/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate")

# Check FileVault status
report["FileVault"] = subprocess.getoutput("/usr/bin/fdesetup status")

# Check latest update from install.log (fallback method)
try:
    log_output = subprocess.check_output(
        "grep 'SUInstallAgent' /var/log/install.log | tail -n 1",
        shell=True,
        text=True
    )
    report["LastUpdate"] = log_output.strip() if log_output else "Unknown"
except Exception as e:
    report["LastUpdate"] = f"Error reading log: {e}"

# Save report
with open("compliance_report_macos.json", "w") as f:
    json.dump(report, f, indent=2)
