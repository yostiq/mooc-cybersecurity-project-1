import sqlite3


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("delete from notes_note where note_text=qwe;")
print('xd')