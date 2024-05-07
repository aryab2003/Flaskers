from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import secrets
import cv2

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "webp", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = secrets.token_hex(16)  # Set your secret key here


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def processImage(filename, operation):
    img = cv2.imread(f"uploads/{filename}")
    match operation:
        case "Grayscale":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f"static/{filename}", gray)
            return filename
        case "JPG":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            cv2.imwrite(f"static/{filename.split('.')[0]}.jpg", img)
            return f"{filename.split('.')[0]}.jpg"  # Return the new JPG filename
        case "PNG":
            cv2.imwrite(f"static/{filename.split('.')[0]}.png", img)
            return f"{filename.split('.')[0]}.png"  # Return the new PNG filename
        case "WEBP":
            cv2.imwrite(f"static/{filename.split('.')[0]}.webp", img)
            return f"{filename.split('.')[0]}.webp"  # Return the new WEBP filename


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            new_filename = processImage(filename, operation)
            flash(f"File uploaded successfully and processed")
            return render_template("index.html", processed_image=new_filename)
    return render_template("index.html")



