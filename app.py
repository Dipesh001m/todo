from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route("/")
def index():
    return "To-Do API is up and running!"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400
    task = {
        "id": len(tasks) + 1,
        "task": data["task"]
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
