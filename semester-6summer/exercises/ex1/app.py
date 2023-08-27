import json, sqlite3, click, functools, os
from flask import Flask, current_app, g, session, redirect, render_template, url_for, request
from flask.cli import with_appcontext

### DATABASE FUNCTIONS ###
def get_db():
    """Returns a connection to the database. On the first run, it initializes the connection"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Closes the connection to the database"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initializes the database with our great SQL schema"""
    db = get_db()
    db.executescript("""
DROP TABLE IF EXISTS firmware;
DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS maybe_infected;

CREATE TABLE firmware (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uploaded DATETIME NOT NULL,
    code TEXT NOT NULL
);

CREATE TABLE device (
    id INTEGER PRIMARY KEY,
    device_key TEXT NOT NULL,
    registration_date DATETIME NOT NULL,
    firmware_id INTEGER NOT NULL,
    FOREIGN KEY (firmware_id) REFERENCES firmware (id)
);

CREATE TABLE contact (
    id1 INTEGER NOT NULL,
    id2 INTEGER NOT NULL,
    proximity INTEGER NOT NULL,
    time_exposed INTEGER NOT NULL,
    FOREIGN KEY (id1) REFERENCES device (id),
    FOREIGN KEY (id2) REFERENCES device (id)
);

CREATE TABLE maybe_infected (
    device_id INTEGER NOT NULL,
    proximity INTEGER NOT NULL,
    time_exposed INTEGER NOT NULL,
    FOREIGN KEY (device_id) REFERENCES device (id)
);

INSERT INTO firmware (uploaded, code) VALUES (datetime('now'), 'thisistotallyfirmwarecode');

INSERT INTO device VALUES (1,'thisisakey',datetime('now'), 1);
INSERT INTO device VALUES (2,'otherkey',datetime('now'), 1);
INSERT INTO device VALUES (3,'wholeotherkey',datetime('now'), 1);

INSERT INTO maybe_infected VALUES (1,0,1000);
INSERT INTO maybe_infected VALUES (2,500,0);
INSERT INTO maybe_infected VALUES (3,4,111000);

""")

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

### APPLICATION SETUP ###
app = Flask(__name__)
app.teardown_appcontext(close_db)
app.cli.add_command(init_db_command)
app.config['DATABASE'] = 'db.sqlite3'
app.secret_key = os.getrandom(32)

### ADMINISTRATOR'S PANEL ###
def login_required(view):
    """Checks that the administrator has logged in, if so it returns the requested view, otherwise
    redirects to the login page"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view

@app.route("/")
@login_required
def index():
    """Main view for the administrator. It shows the registered devices, and all devices of users
    that have potentially been infected. For privacy, we hide the table of all contacts to the
    administrator."""
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM device")
    devices = "\n".join(
        f"<tr><td>{d['id']}</td><td>{d}</td><td>{d['registration_date']}</td><td>{d['firmware_id']}            </td></tr>"
        for d in c.fetchall())
    c.execute("SELECT * FROM maybe_infected")
    infected = "\n".join(
        f"<tr><td>{i['device_id']}</td><td>{i['proximity']}</td><td>{i['time_exposed']}</td></tr>"
        for i in c.fetchall())
    return f"""<!DOCTYPE html>
<html>
    <head><title>CoviDIoT - Overview </title></head>
    <body><h1>CoviDIoT - Overview</h1>
        <h2>Device list:</h2>
        <table>
        <tr><th>Device ID</th><th>Key</th><th>Registration date</th><th>Firmware ID</th></tr>
        {devices}
        </table>
        <h2>Maybe infected:</h2>
        <table>
        <tr><th>Device ID</th><th>Proximity</th><th>Time exposed</th></tr>
        {infected}
        </table>
        <h2>Upload new firmware:</h2>
        <form method=POST action=/upload_firmware/ enctype=multipart/form-data>
        <input type=file name=code/>
        <button type=submit value=Upload/>
        </form>
        <div><a href="/logout/">Logout</a>
    </body>
</html>"""
supersecretpassword = 'ool0AeR0'


def passcheck(user, password):
    return eval("'%s' == 'admin' and '%s' == supersecretpassword" % (user,password))

@app.route("/login/", methods=('GET', 'POST'))
def login():
    """Login page: requires the administrator to put a very secure password"""
    message = ""
    if request.method == 'POST':
	
        username = request.form['username']
        password = request.form['password']

        if passcheck(username,password):
            #if username == 'admin' and password == 'ool0AeR0':
            # TODO: we should think of a better authentication method
            session.clear()
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            message = "Username and password did not match!"
    return f"""<!DOCTYPE html>
<html>
    <head><title>CoviDIoT - Login </title></head>
    <body>
        <h1>CoviDIoT - Login</h1>
        {message}
        <form method=POST>
            Username: <input type="text" name="username"/><br/>
            Password: <input type="password" name="password"/><br/>
            <button>Login</button>
        </form>
    </body>
</html>"""

@app.route("/logout/")
@login_required
def logout():
    """Logout: clears the session"""
    session.clear()
    return redirect(url_for('index'))

@app.route("/upload_firmware/", methods=('POST',))
def upload_firmware():
    """Last administrator's functionality: it allows to upload a new firmware from the app developer"""
    code = request.files['code/'].read()
    db = get_db()
    c = db.cursor()
    c.execute("INSERT INTO firmware (uploaded, code) VALUES (datetime('now'), ?)", (code,))
    db.commit()
    return redirect("/")

### DEVICE API ###
@app.route("/api/register_device/", methods=('POST',))
def register_device():
    """Allows a new shiny CoviDIoT client to be registered on this platform"""
    db = get_db()
    c = db.cursor()
    try:
        device_id = request.form['device_id']
        key = request.form['key']
        firmware_id = request.form['firmware_id']
        c.execute("INSERT INTO device VALUES (" + device_id + ", " + key + ", datetime('now'), " + 
            firmware_id + ")")
        db.commit()
        return (json.dumps({"result": "OK"}))
    except Exception as e:
        return (json.dumps({"result": "Error", "message": str(e)}))

@app.route("/api/register_contact/", methods=('POST',))
def register_contact():
    """Registers a contact between devices `id1` and `id2`. Needs `id1`'s secret key to execute."""
    db = get_db()
    c = db.cursor()
    try:
        id1 = request.form['id1']
        key = request.form['key']
        id2 = request.form['id2']
        proximity = request.form['proximity']
        time_exposed = request.form['time_exposed']
        c.execute("SELECT * FROM device WHERE id = ? AND device_key = ?", (id1, key))
        if c.fetchone():
            c.execute("INSERT INTO contact VALUES (?, ?, ?, ?)", (id1, id2, proximity, time_exposed))
            db.commit()
            return (json.dumps({"result": "OK"}))
        else:
            return (json.dumps({"result": "Error", "message": "Wrong device ID or key"}))
    except Exception as e:
        return (json.dumps({"result": "Error", "message": str(e)}))

@app.route("/api/signal_positive/", methods=('POST',))
def signal_positive():
    """Signals that `id1` has tested positive. Needs `id1`'s secret key to execute.
    For privacy, once a device's owner has tested positive, we remove all their contacts from the
    `contact` table, and only keep the other device ID `id2` on the `maybe_infected` table."""
    db = get_db()
    c = db.cursor()
    try:
        id1 = request.form['id1']
        key = request.form['key']
        c.execute("SELECT * FROM device WHERE id = ? AND device_key = ?", (id1, key))
        if c.fetchone():
            # Inserting those who got exposed to id1 into maybe_infected
            c.execute("INSERT INTO maybe_infected SELECT id2, proximity, time_exposed FROM contact                        WHERE id1 = ?", (id1,))
            # For privacy, we erase all the records of those who got in contact with id1
            c.execute("DELETE FROM contact WHERE id1 = ?", (id1,))
            db.commit()
            return (json.dumps({"result": "OK"}))
        else:
            return (json.dumps({"result": "Error", "message": "Wrong device ID or key"}))
    except Exception as e:
        return (json.dumps({"result": "Error", "message": str(e)}))

@app.route("/api/am_i_infected/", methods=('POST',))
def am_i_infected():
    db = get_db()
    c = db.cursor()
    try:
        device_id = request.form['device_id']
        key = request.form['key']
        c.execute("SELECT * FROM device WHERE id = ? AND device_key = ?", (device_id, key))
        if c.fetchone():
            c.execute("SELECT * FROM maybe_infected WHERE device_id = ?", (device_id,))
            exposures = c.fetchall()
            if exposures:
                data = []
                for row in exposures:
                    data.append(list(row)) # or simply data.append(list(row))
                return (json.dumps({"result": "Yes", "exposures": data}))
            else:
                return (json.dumps({"result": "No"}))
        else:
            return (json.dumps({"result": "Error", "message": "Wrong device ID or key"}))
    except Exception as e:
        return (json.dumps({"result": "Error", "message": str(e)}))

@app.route("/api/get_latest_firmware/")
def get_latest_firmware():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM firmware ORDER BY uploaded DESC LIMIT 1")
    firmware = c.fetchone()
    return (json.dumps({"result": "OK", "firmware": firmware['code']}))
