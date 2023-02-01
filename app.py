
from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    data = cur.execute(
        "SELECT * FROM todolist",
    ).fetchall()
    print(data)

    return render_template('hello_world.html',data = data)
 


def init_db():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
   
    cur.execute(
        "CREATE TABLE IF NOT EXISTS todolist (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, description text, done boolean)"
    )
    ToDoList = [{"name":"buy drinks","description":"coke","done":False},{"name":"buy meds","description":"pandol","done":False},{"name":"buy food","description":"bread","done":False}]

    # Fill models table
    for thing in ToDoList:
        cur.execute(
            "INSERT OR IGNORE INTO ToDoList (name, description,done) VALUES (?, ?,?)",
            (thing["name"], thing["description"],thing["done"]),
        )
    con.commit()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    
