from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("medicine.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    district = request.args.get("district", "")
    address = request.args.get("address", "")

    conn = get_db()
    boxes = conn.execute("""
        SELECT * FROM box
        WHERE district LIKE ? AND address LIKE ?
    """, (f"%{district}%", f"%{address}%")).fetchall()
    conn.close()

    return render_template("index.html", boxes=boxes)
if __name__ == "__main__":
    app.run()
