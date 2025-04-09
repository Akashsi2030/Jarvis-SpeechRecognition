from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    user_command = request.form.get("command")
    try:
        # Pass the command to your JARVIS backend
        subprocess.Popen(["python", "JARVIS_index.py", user_command])
        return jsonify({"status": f"Executing: {user_command}"})
    except Exception as e:
        return jsonify({"status": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
