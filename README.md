# CISS - IoT Device Security Scoring System

**Group Number: 03**

CISS is an IoT device security scoring system designed to provide a risk score based on common threats found in Internet of Things environments.
The scoring is based on 15 predefined metrics derived from the Mirai botnet malware, whose source code is publicly available. Each metric is assigned a weight according to how critical the vulnerability is—e.g., physical tampering is considered less risky compared to insecure online exposure.

---

## Files in the Repository

* **app.py**
  A Python Flask backend file that implements the scoring logic. It receives a parsed JSON file containing the user-inputted IoT device security data. The backend multiplies the input with predefined weightage values and calculates a final score.
  These weightages are hardcoded and based on the prioritization of vulnerabilities (e.g., default credentials are riskier than lack of physical security).

* **index.html**
  A front-end file that acts as the GUI. It takes user input for each metric (Low, Medium, or High) using dropdowns. When the user presses the submit button, the data is converted to JSON and sent to the backend (app.py).


---

## How to Run the Project

1. Install Python and Flask:

   ```
   pip install flask
   ```

2. Run the Flask backend:

   ```
   python app.py
   ```

3. Open your browser and go to:

   ```
   http://localhost:5000
   ```

4. Enter the severity levels for each metric and submit.
   The backend calculates the final score and returns a risk category (Low, Medium, or High) with a recommendation.

---

## Tools and Technologies Used

* Flask (Python) – for the backend
* HTML/CSS – for the frontend
* JSON – for data transfer
* MP4 (Screen Demo) – for visualization and testing

---

