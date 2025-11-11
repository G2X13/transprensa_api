from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"status": "ok", "message": "API Transprensa funcionando correctamente"}

@app.route("/transprensa/login", methods=["POST"])
def login_transprensa():
    url = "https://transprensa.colombiasoftware.net/index.php?api=servicio.Seguridad.login"
    data = {
        "usuario_login": "WSINCOLMOTOS",
        "usuario_password": "Incolmotos2025"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        r = requests.post(url, data=data, headers=headers)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
