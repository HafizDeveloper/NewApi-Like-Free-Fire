import os
import requests
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ini yang Hafiz nak: Endpoint /api/like
@app.route('/api/like', methods=['GET'])
def simple_like():
    # Ambil UID dari link (?uid=xxxx)
    uid = request.args.get('uid')
    
    if not uid:
        return jsonify({
            "status": "error",
            "message": "Mana UID? Sila letak ?uid=NOMBOR_ID kat hujung link"
        }), 400

    # Maklumat Header (Kunci akses Polar Bear)
    target_url = "https://clientbp.ggpolarbear.com/LikeProfile"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo2MjM4NjIxMTQ0LCJuaWNrbmFtZSI6IkRFVuOFpEhBRklaIiwibm90aV9yZWdpb24iOiJTRyIsImxvY2tfcmVnaW9uIjoiU0ciLCJleHRlcm5hbF9pZCI6IjM3Yzc2MmViNzFlYzEyMWYxODhhNWZlOGIwZTgyZWQ5IiwiZXh0ZXJuYWxfdHlwZSI6MywicGxhdF9pZCI6MSwiY2xpZW50X3ZlcnNpb24iOiIxLjExOC4xNiIsImVtdWxhdG9yX3Njb3JlIjoxMDAsImlzX2VtdWxhdG9yIjp0cnVlLCJjb3VudHJ5X2NvZGUiOiJNWSIsImV4dGVybmFsX3VpZCI6MTIxMjUzNTk3MjMzNzAyLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDQsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTY1MjAwOTQwNCwiY2xpZW50X3R5cGUiOjIsInNpZ25hdHVyZV9tZDUiOiI3NDI4YjI1M2RlZmMxNjQwMThjNjA0YTFlYmJmZWJkZiIsInVzaW5nX3ZlcnNpb24iOjEsInJlbGVhc2VfY2hhbm5lbCI6ImFuZHJvaWQiLCJyZWxlYXNlX3ZlcnNpb24iOiJPQjUxIiwiZXhwIjoxNzY2NTQ2MDU5fQ.SmUu4caMkQFixBHZvPFnD4j2pS35k1q9HXWZ-GenpkU",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)"
    }

    # Payload (PENTING: Ini kod rahsia yang kita bincang tadi)
    raw_payload = b'\xc9\xb4\xd9Q\x18?\xb4\xed\xcb;\xee\xc7\xe6\x06\xde\xc2'

    try:
        # Kita hantar 1 request (atau buat loop kalau nak banyak)
        response = requests.post(target_url, headers=headers, data=raw_payload, timeout=5)
        
        if response.status_code == 200:
            return jsonify({
                "status": "success",
                "uid": uid,
                "message": "Like berjaya dihantar!",
                "developer": "Hafiz"
            })
        else:
            return jsonify({
                "status": "failed",
                "reason": "Token Expired atau Server Down"
            }), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
