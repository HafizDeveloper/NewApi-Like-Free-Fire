import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary storage in RAM
task_queue = []

@app.route('/')
def index():
    return jsonify({
        "status": "online",
        "message": "Free Fire Like API"
    })

@app.route('/api/like', methods=['GET'])
def add_to_queue():
    uid = request.args.get('uid')
    key = request.args.get('key')
    region = request.args.get('server', 'SINGAPORE').upper()

    # Security Key Check
    if key != "HAFIZ77":
        return jsonify({
            "success": False,
            "message": "Invalid API Key"
        }), 403

    if not uid:
        return jsonify({
            "success": False,
            "message": "UID parameter is missing"
        }), 400 

    # Add task to queue
    task = {"uid": uid, "server": region}
    task_queue.append(task)

    return jsonify({
        "success": True,
        "message": "UID added to queue",
        "data": {
            "uid": uid,
            "server": region,
            "queue_size": len(task_queue)
        }
    })

@app.route('/get_task', methods=['GET'])
def get_task():
    if task_queue:
        return jsonify(task_queue.pop(0))
    return jsonify({"uid": None})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)