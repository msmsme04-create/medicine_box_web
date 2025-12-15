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


@app.route("/add", methods=["POST"])
def add():
    district = request.form["district"]
    name = request.form["name"]
    address = request.form["address"]
    detail = request.form["detail"]

    conn = get_db()
    conn.execute("""
        INSERT INTO box (district, name, address, detail)
        VALUES (?, ?, ?, ?)
    """, (district, name, address, detail))
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM box WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    new_detail = request.form["detail"]

    conn = get_db()
    conn.execute("""
        UPDATE box
        SET detail = ?
        WHERE id = ?
    """, (new_detail, id))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/edit/<int:id>")
def edit(id):
    conn = get_db()
    box = conn.execute(
        "SELECT * FROM box WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    return render_template("edit.html", box=box)

@app.route("/report/<int:box_id>", methods=["POST"])
def report(box_id):
    content = request.form["content"]

    conn = get_db()
    conn.execute("""
        INSERT INTO report (box_id, content, created_at)
        VALUES (?, ?, ?)
    """, (box_id, content, datetime.now()))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run()
