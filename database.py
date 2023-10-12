import sqlite3 as sq


async def db_start():
    global db, cur
    db = sq.connect('iqtibos.db')
    cur = db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER, 
                username TEXT)''')
    
    db.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS templates(
                i_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT,
                dt DATETIME DEFAULT CURRENT_TIMESTAMP,
                number TEXT,
                desc TEXT)''')
    db.commit()




async def cmd_start_db(user_id):
    db = sq.connect('iqtibos.db')
    cur = db.cursor()
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()


async def add_template(state,user_id):
    db = sq.connect('iqtibos.db')
    cur = db.cursor()
    async with state.proxy() as data:
        cur.execute("INSERT INTO templates (user, number, desc) VALUES (?, ?, ?)",
                    (user_id, data['template_number'], data['title']))
        db.commit()


#cheking if user exists
async def user_number():
    db = sq.connect('iqtibos.db')
    cur = db.cursor()
    fetch = cur.execute('SELECT id FROM users').fetchall()
    return fetch


async def add_user(user):
    db = sq.connect('iqtibos.db')
    cur = db.cursor()
    cur.execute("INSERT INTO users (tg_id, username) VALUES (?, ?)",(user))
    db.commit()


