import os
import subprocess
from flask import Flask, request, render_template_string, send_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


HTML = """
<!doctype html>
<title>TOPSIS Web</title>
<h2>TOPSIS Calculator</h2>

<form method=post enctype=multipart/form-data>
  <p>Input File: <input type=file name=file required></p>
  <p>Weights (comma separated): <input type=text name=weights required></p>
  <p>Impacts (comma separated): <input type=text name=impacts required></p>
  <p><input type=submit value=Submit></p>
</form>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

        file.save(input_path)

        cmd = [
            "topsis",
            input_path,
            weights,
            impacts,
            output_path,
        ]

        subprocess.run(cmd)

        return send_file(output_path, as_attachment=True)

    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
