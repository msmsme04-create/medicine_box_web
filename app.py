from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("medicine.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db()
    boxes = conn.execute("SELECT * FROM box").fetchall()
    conn.close()
    return render_template("index.html", boxes=boxes)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    address = request.form["address"]

    conn = get_db()
    conn.execute(
        "INSERT INTO box (name, address) VALUES (?, ?)",
        (name, address)
    )
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM box WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)