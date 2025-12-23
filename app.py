import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/like', methods=['GET'])
def simple_like():
    uid = request.args.get('uid')
    region = request.args.get('region', default='sg') # Default region SG
    
    if not uid:
        return jsonify({"status": "error", "message": "UID diperlukan"}), 400

    # Kita guna 'Public Engine' yang lebih senang hantar Like guna UID terus
    # Saya gunakan format URL yang biasa digunakan oleh bot-bot Like besar
    engine_url = f"https://freefire-api.vercel.app/api/like?uid={uid}&region={region}"

    try:
        # API Render Hafiz akan panggil engine ni
        response = requests.get(engine_url, timeout=10)
        data = response.json()

        # Kalau engine tu berjaya
        if response.status_code == 200:
            return jsonify({
                "status": "success",
                "uid": uid,
                "nickname": data.get("nickname", "Player"),
                "message": "Like Berjaya Dihantar!",
                "developer": "Hafiz Bot"
            })
        else:
            return jsonify({
                "status": "failed",
                "message": "Server Like sedang sibuk (Limit). Cuba lagi nanti."
            }), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
