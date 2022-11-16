import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
##curs.execute(''' CREATE TABLE books
##(title VARCHAR(150) PRIMARY KEY,
##author VARCHAR(150),
##year INT)''')

##conn.execute('INSERT INTO books  VALUES ("The Weirdstone of Brisingamen", "Alan Garner", 1960)')
##conn.execute('INSERT INTO books  VALUES ("Perdido Street Station", "China Miéville", 2000)')
##conn.execute('INSERT INTO books  VALUES ("Thud!", "Terry Pratchett", 2005)')
##conn.execute('INSERT INTO books  VALUES ("The Spellman Files", "Lisa Lutz", 2007)')
##conn.execute('INSERT INTO books  VALUES ("Small Gods", "Terry Pratchett", 1992)')

curs.execute('SELECT * FROM books')
rows = curs.fetchall()
print(rows)