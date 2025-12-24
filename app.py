import os
import requests
import binascii
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Koleksi payload hex yang Hafiz tangkap tadi
PAYLOADS = [
    "330c58f69b52b20039055ba810d05f7a",
    "8bad3f3af0cd001e2d3c784f31868bcc"
]

@app.route('/api/like', methods=['GET'])
def simple_like():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID diperlukan!"}), 400

    target_url = "https://clientbp.ggpolarbear.com/LikeProfile"
    
    # TOKEN BARU HAFIZ (KuihBiadap1)
    token = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxNDE2NjI0NzQ3MCwibmlja25hbWUiOiJLdWloQmlhZGFwMSIsIm5vdGlfcmVnaW9uIjoiU0ciLCJsb2NrX3JlZ2lvbiI6IlNHIiwiZXh0ZXJuYWxfaWQiOiI5OTdmMTJkYTA4MWVmYjhiM2M3NmM4OWExY2ZlODViZSIsImV4dGVybmFsX3VpZCI6NCwicGxhdF9pZCI6MSwiY2xpZW50X3ZlcnNpb24iOiIxLjExOC4xNiIsImVtdWxhdG9yX3Njb3JlIjoxMDAsImlzX2VtdWxhdG9yIjp0cnVlLCJjb3VudHJ5X2NvZGUiOiJNWSIsImV4dGVybmFsX3VpZCI6NDM1MTAyNjY1MCwicmVnX2F2YXRhciI6MTAyMDAwMDA3LCJzb3VyY2UiOjAsImxvY2tfcmVnaW9uX3RpbWUiOjE3NjYyMDk1MjcsImNsaWVudF90eXBlIjoyLCJzaWduYXR1cmVfbWQ1IjoiNzQyOGIyNTNkZWZjMTY0MDE4YzYwNGExZWJiZmViZGYiLCJ1c2luZ192ZXJzaW9uIjoxLCJyZWxlYXNlX2NoYW5uZWwiOiJhbmRyb2lkIiwicmVsZWFzZV92ZXJzaW9uIjoiT0I1MSIsImV4cCI6MTc2NjYyMzA4OX0.R3MdRWdTSGH_z5oE0mdAN6ZaqSZKRPtEiS_XtWfL_Xg"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.1; ONEPLUS A5000 Build/NMF26X)"
    }

    success_count = 0
    # Cuba hantar semua payload yang kita ada
    for hex_str in PAYLOADS:
        try:
            raw_data = binascii.unhexlify(hex_str)
            response = requests.post(target_url, headers=headers, data=raw_data, timeout=5)
            if response.status_code == 200:
                success_count += 1
        except:
            continue

    if success_count > 0:
        return jsonify({
            "status": "success",
            "uid": uid,
            "nickname": "KuihBiadap1", # Akaun yang hantar like
            "message": f"Berjaya hantar {success_count} Like request!"
        })
    else:
        return jsonify({
            "status": "failed",
            "message": "Server reject request. Mungkin payload sudah basi."
        })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
