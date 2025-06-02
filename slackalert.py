# Sends Slack alert if non-compliance is detected
# Save as slack_alert.py

import json, requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

def check_noncompliance():
    alerts = []
    with open("compliance_report_win.json") as f:
        data = json.load(f)
        for fw in data["Firewall"]:
            if not fw["Enabled"]:
                alerts.append(f"Firewall {fw['Name']} is OFF")

        if not data["Antivirus"]["AntivirusEnabled"]:
            alerts.append("Antivirus is OFF")

        if data["BitLocker"]["ProtectionStatus"] != "On":
            alerts.append("BitLocker not protecting drive")

    return alerts

def send_alerts(alerts):
    if alerts:
        msg = "⚠️ *Non-compliance detected:*\n" + "\n".join(f"- {a}" for a in alerts)
        requests.post(SLACK_WEBHOOK_URL, json={"text": msg})

alerts = check_noncompliance()
send_alerts(alerts)
