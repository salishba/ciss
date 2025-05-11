CISS - IoT Device Security Scoring System

CISS is a lightweight scoring system to calculate the security risk of IoT devices. The scoring is based on common threats from the Mirai botnet malware (open source available) and assigns weights to different types of vulnerabilities based on how serious they are.

---

### 🔧 What’s in the repo:

* `app.py`
  Python Flask backend file. Handles the logic for scoring.

  * It receives data as JSON (parsed from the HTML form).
  * Multiplies user-selected values (Low, Medium, High → converted to numbers) with predefined weights.
  * These weights are based on how risky each vulnerability is (e.g., physical tampering is low risk, internet exposure is high).

* `index.html`
  Frontend form for the user to select the severity of each vulnerability.

  * On submit, sends the values as a JSON payload to Flask backend.
  * Displays final risk score and message (Low, Medium, High).

* `report.pdf`
  Describes all the 15 metrics used in the scoring system, what they mean, and why they were weighted a certain way.

---

### 💡 How it works:

* User selects severity (e.g., Low/Medium/High) for each metric in the form.
* Values get sent to `app.py` using JavaScript as a JSON file.
* Flask receives the data, calculates a final score using:
  `score = sum(weight * metric)`
* Returns a message:

  * 0–3 = High Risk (needs fixing now)
  * 4–6 = Medium Risk (mitigation recommended)
  * 7–10 = Low Risk (secure but still needs monitoring)

---

### 🖥️ To run:

1. Install Flask
   `pip install flask`

2. Run the backend
   `python app.py`

3. Open browser at
   `http://localhost:5000`

---

Let me know if you want me to format this directly as a `README.md` file for your repo!
