import sqlite3

class Library:

    def __init__(self):
        self.connection=sqlite3.connect("data1.db")
        self.cursor=self.connection.cursor()
        self.create_tabels()
          
    def create_tabels(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books
                               (name_book TEXT, author TEXT, year INTEGER, pages INTEGER, book_id INTEGER PRIMARY KEY)""")
            
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS members
                                (name_member TEXT, age INTEGER, member_id INTEGER PRIMARY KEY,
                                FOREIGN KEY(member_id) REFERENCES books(id_number))""")
            
        self.cursor.execute("CREATE  TABLE IF NOT EXISTS borrow (book_id INTEGER, member_id INTEGER)")
        
# ************book************
    def add_books(self, add_book):
        self.cursor.execute("""INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?, ?)""",add_book)
        self.connection.commit()
        
        
    def books_list(self):
        books_list=self.connection.execute("SELECT * FROM books").fetchall()
        for book in books_list:
            print(book)

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE book_id = (?)", (book_id,))
        self.connection.commit()
        

    def search_author(self, author):
        print(self.cursor.execute("SELECT * FROM books WHERE author = (?)", (author,)).fetchall())
        
    
    def search_book(self, name_book):
        print(self.cursor.execute("SELECT * FROM books WHERE name_book = (?)", (name_book,)).fetchone())


# ************member************
    def add_member(self, add_member):
        self.cursor.execute("INSERT OR IGNORE INTO members VALUES (?, ?, ?)", (add_member))
        self.connection.commit()
        
        
    def search_member(self, name_member):
        print(self.cursor.execute("SELECT * FROM members WHERE name_member = (?)", (name_member,)).fetchall())
    
    def delete_member(self, member_id):
        self.cursor.execute("DELETE FROM members WHERE member_id = (?)", (member_id,))
        self.connection.commit()
        

#************borrow************
    def create_borrow(self, member_id, book_id):
        max_borrow=self.cursor.execute("SELECT COUNT(member_id) FROM borrow WHERE member_id = (?)", (member_id,)).fetchone()
        if max_borrow[0]<2:
            self.cursor.execute("INSERT OR IGNORE INTO borrow VALUES (?,?)", (book_id, member_id))
            self.connection.commit()
        else:
            print("You reach the MAX")
            
    
    def borrow_list(self):
        brw_list=self.cursor.execute("SELECT books.name_book, books.author, members.name_member, members.member_id FROM borrow INNER JOIN books ON borrow.book_id=books.book_id INNER JOIN members on borrow.member_id=members.member_id  ").fetchall()
        for borrow in brw_list:
            print(borrow)

    def close_connection(self):
        self.connection.close()
