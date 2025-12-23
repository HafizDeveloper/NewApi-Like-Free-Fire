import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/like', methods=['GET'])
def simple_like():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID diperlukan"}), 400

    target_url = "https://clientbp.ggpolarbear.com/LikeProfile"
    
    # Token ni mungkin dah mati, Hafiz kena ambil yang baru dari mitmweb kalau error tetap sama
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo2MjM4NjIxMTQ0LCJuaWNrbmFtZSI6IkRFVuOFpEhBRklaIiwibm90aV9yZWdpb24iOiJTRyIsImxvY2tfcmVnaW9uIjoiU0ciLCJleHRlcm5hbF9pZCI6IjM3Yzc2MmViNzFlYzEyMWYxODhhNWZlOGIwZTgyZWQ5IiwiZXh0ZXJuYWxfdHlwZSI6MywicGxhdF9pZCI6MSwiY2xpZW50X3ZlcnNpb24iOiIxLjExOC4xNiIsImVtdWxhdG9yX3Njb3JlIjoxMDAsImlzX2VtdWxhdG9yIjp0cnVlLCJjb3VudHJ5X2NvZGUiOiJNWSIsImV4dGVybmFsX3VpZCI6MTIxMjUzNTk3MjMzNzAyLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDQsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTY1MjAwOTQwNCwiY2xpZW50X3R5cGUiOjIsInNpZ25hdHVyZV9tZDUiOiI3NDI4YjI1M2RlZmMxNjQwMThjNjA0YTFlYmJmZWJkZiIsInVzaW5nX3ZlcnNpb24iOjEsInJlbGVhc2VfY2hhbm5lbCI6ImFuZHJvaWQiLCJyZWxlYXNlX3ZlcnNpb24iOiJPQjUxIiwiZXhwIjoxNzY2NTQ2MDU5fQ.SmUu4caMkQFixBHZvPFnD4j2pS35k1q9HXWZ-GenpkU",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)"
    }

    # Payload hex rahsia
    raw_payload = b'\xc9\xb4\xd9Q\x18?\xb4\xed\xcb;\xee\xc7\xe6\x06\xde\xc2'

    try:
        # Kita buat request dan check status terus
        response = requests.post(target_url, headers=headers, data=raw_payload, timeout=10)
        
        # Kalau server Polar Bear balas (walaupun error 401/403)
        return jsonify({
            "status": "connected",
            "uid_requested": uid,
            "server_response_code": response.status_code,
            "server_msg": response.text[:100], # Ambil sikit je text dari server
            "developer": "Hafiz"
        })

    except Exception as e:
        # Kalau internet Render bermasalah atau timeout
        return jsonify({
            "status": "error",
            "error_detail": str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
