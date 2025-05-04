from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print("Received data:", data)

     
    w1 = 0.10
    w2 = 0.08
    w3 = 0.10
    w4 = 0.08
    w5 = 0.06
    w6 = 0.05
    w7 = 0.07
    w8 = 0.10
    w9 = 0.06
    w10 = 0.08   
    w11 = 0.06
    w12 = 0.05
    w13 = 0.10
    w14 = 0.05
    w15 = 0.06

    m1 = float(data.get("deviceExposureLevel", 0) or 0)
    m2 = float(data.get("attackSurfaceComplexity",0) or 0)
    m3 = float(data.get("defaultCredentials",0) or 0)
    m4 = float(data.get("firmwareUpdateMechanism",0) or 0)
    m5 = float(data.get("vulnDisclosurePatchTime",0) or 0)
    m6 = float(data.get("codeIntegrity",0) or 0)
    m7 = float(data.get("accessControlGranularity",0) or 0)
    m8 = float(data.get("encryption",0) or 0)
    m9 = float(data.get("deviceIdentity",0) or 0)
    m10 = float(data.get("supplyChainTrust",0) or 0)
    m11 = float(data.get("hardwareSecurity",0) or 0)
    m12 = float(data.get("sideChannelResistance",0) or 0)
    m13 = float(data.get("exploitability",0) or 0)
    m14 = float(data.get("threatActorInterest",0) or 0)
    m15 = float(data.get("physicalSecurity",0) or 0)

    score = score = ((w1 * m1) + (w2 * m2) + (w3 * m3) + (w4 * m4) + (w5 * m5) + (w6 * m6) + (w7 * m7) + (w8 * m8) + (w9 * m9) + (w10 * m10) + (w11 * m11) + (w12 * m12) + (w13 * m13) + (w14 * m14) + (w15 * m15))

    message = ""

    if score >= 0 and score <= 3:
        message = "Low Risk (No Urgent Action Required)"
    elif score > 3 and score <= 6:
        message = "Moderate Risk (Patch vulnerabilities, Improve Security)"
    elif score > 6 and score <= 11:
        message = "High Risk (Immediate Action Required)"


    print(f"{message}")

    return jsonify({
        "score": round(score, 2),
        "message": message,
    }), 200


if __name__ == '__main__':
    app.run(debug=True)