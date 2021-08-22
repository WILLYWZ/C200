import sqlite3

dog = sqlite3.connect("example1.db")
c = dog.cursor()
r = [('c','a'),('a','b'), ('a','e'),('c','d'),
     ('c','f'),('f','g'), ('f','h'),('h','j'),
     ('h','i')]

c.execute('''CREATE TABLE G (Parent text, Child)''')

c.executemany('INSERT INTO G VALUES (?,?)', r)

dog.commit()


q = lambda x, y: "parent from " if c.exucute(fetchall_sql,x).fetchlone()==\
        c.exucute(fetchall_sql,x).fetchlone() else ""

print(c.execute(q('b','e')).fetchone())
print(c.execute(q('h','g')).fetchone())
print(c.execute(q('e','a')).fetchone())

dog.close()