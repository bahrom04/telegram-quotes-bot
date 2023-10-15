import sqlite3 as sq


def connect_db():
    global db, cur
    db = sq.connect('iqtibos.db')
    


async def db_start():
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id TEXT PRIMARY KEY,
                full_name TEXT,)''')
    
    db.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS templates(
                i_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                user TEXT PRIMARY KEY,
                dt DATETIME DEFAULT CURRENT_TIMESTAMP,
                number TEXT,
                desc TEXT)''')
    db.commit()




async def cmd_start_db(user_id):
    # db = connect_db()
    cur = db.cursor()
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()


# Log of context
async def add_template(state,full_name,user_id):
    # db = connect_db()
    cur = db.cursor()
    async with state.proxy() as data:
        cur.execute("INSERT INTO templates (full_name, user, number, desc) VALUES (?, ?, ?, ?)",
                    (full_name, user_id, data['template_number'], data['title']))
        db.commit()


#cheking if user exists
def user_number():
    # db = connect_db()
    cur = db.cursor()
    fetch = cur.execute('SELECT user_id FROM users').fetchall()
    ids = [i[0] for i in fetch]
    return ids


# Add new user to the database after start
def add_user(user):
    # db = connect_db()
    cur = db.cursor()
    cur.execute("INSERT INTO users (user_id, full_name) VALUES (?, ?)",(user))
    db.commit()


