# 🔐 Automated Endpoint Security Compliance Checker

Cross-platform auditing and compliance reporting toolkit for Windows and macOS endpoints in enterprise environments.

## 📌 Features

✅ Windows PowerShell script for:
- Firewall profile status
- Microsoft Defender/Antivirus health
- BitLocker encryption check (C: drive)
- Latest system patch install date

✅ macOS Python script for:
- macOS Firewall status
- FileVault disk encryption
- OS update detection from system logs

✅ Flask Dashboard:
- View both Windows/macOS reports in-browser
- Easily monitor compliance from one interface

✅ Slack Alerts (Optional):
- Notify IT staff if devices fall out of compliance (e.g., disabled antivirus, no encryption)

---

## 🛠 Technology Stack

- **Windows:** PowerShell 5+
- **macOS:** Python 3.8+, Bash
- **Backend:** Flask (Python)
- **Frontend:** HTML (Jinja2 Template)
- **Notifications:** Slack Webhook API
- **Output:** JSON reports, real-time alerts

---

## 🚀 Quickstart

### 🪟 For Windows

1. Open PowerShell as Administrator  
2. Run:
```powershell
.\check_compliance_windows.ps1
Output: compliance_report_win.json (saved on Desktop)

🍎 For macOS
Run:

bash
Copy
Edit
python3 check_compliance_macos.py
Output: compliance_report_macos.json

Tip: Use sudo if needed to access /var/log/install.log

🌐 Flask Dashboard
Install Flask:

bash
Copy
Edit
pip install flask
Project structure:

pgsql
Copy
Edit
project/
│
├── dashboard.py
├── compliance_report_win.json
├── compliance_report_macos.json
└── templates/
    └── index.html
Run the dashboard:

bash
Copy
Edit
python3 dashboard.py
Open in browser: http://localhost:5000

💬 Slack Alert (Optional)
Get your Slack Incoming Webhook URL

Paste into slack_alert.py:

python
Copy
Edit
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/..."
Run:

bash
Copy
Edit
python3 slack_alert.py
📂 Sample Output
compliance_report_win.json
json
Copy
Edit
{
  "Hostname": "WIN-1234",
  "Firewall": [
    {"Name": "Domain", "Enabled": true},
    {"Name": "Private", "Enabled": true},
    {"Name": "Public", "Enabled": false}
  ],
  ...
}
compliance_report_macos.json
json
Copy
Edit
{
  "hostname": "MacBook-Pro.local",
  "FileVault": "FileVault is On.",
  "Firewall": "Firewall is enabled. (State = 1)",
  ...
}
✅ Use Cases
University IT endpoint compliance

Corporate security audits

BYOD/remote laptop policy enforcement

Patch & encryption enforcement visibility

📈 Benefits
🚫 Avoids manual endpoint checks

🔄 Automates routine IT policy validation

🔔 Alerts IT team of vulnerabilities instantly

💻 Supports both Windows and macOS fleets

🧩 Extensible (add Linux, email reports, AD sync)

📃 License
MIT License

