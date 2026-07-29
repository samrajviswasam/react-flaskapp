from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__,
            static_folder="static",
            static_url_path="")

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask app backend is running successfully"})

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)

    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
