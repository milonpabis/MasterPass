import sqlite3
import sqlite3 as db


class DataBaseControl:

    def __init__(self):
        self.connection = db.connect("data/users.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS Users(
        Mail VARCHAR(35),
        Username VARCHAR(30) UNIQUE,
        Password VARCHAR(40));
        """)
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS Data(
        Username VARCHAR(30),
        Site VARCHAR(20),
        Login VARCHAR(30),
        Password VARCHAR(40));
        """)

    def add_user(self, email, username, password):
        self.cursor.execute(f"INSERT INTO Users VALUES ('{email}', '{username}', '{password}')")
        self.connection.commit()

    def return_data(self, username):
        res = self.cursor.execute(f"SELECT Data.Site, Data.Login, Data.Password FROM Data, Users WHERE Data.Username "
                                  f"= Users.Username AND Data.Username = '{username}'")

        return res.fetchall()

    def return_users(self):
        res = self.cursor.execute(f"SELECT Users.Username, Users.Password FROM Users")
        return res.fetchall()


    def add_password(self, user, site, login, password):
        self.cursor.execute(f"INSERT INTO Data VALUES ('{user}', '{site}', '{login}', '{password}')")
        self.connection.commit()

    def delete_password(self, user, site, login, password):
        self.cursor.execute(f"DELETE FROM Data WHERE Username = '{user}' AND Site = '{site}' AND Login = '{login}' "
                            f"AND Password = '{password}'")
        self.connection.commit()

    def update_password(self, user, site, login, password, old_site, old_login, old_password):
        print(user, site, login, password, old_site, old_login, old_password)
        self.cursor.execute(f"UPDATE Data SET Site='{site}', Login='{login}', Password='{password}' WHERE "
                            f"Username='{user}' AND Site='{old_site}' AND Login='{old_login}' AND"
                            f" Password='{old_password}'")
        self.connection.commit()


# if __name__ == "__main__":
#     db = DataBaseControl()
#     try:
#         db.add_user('miloszpabis@onet.pl', 'milonpabis', 'kurwa123')
#     except sqlite3.IntegrityError:
#         print('this account exists')
#     #db.add_password('milonpabis', 'Facebook', 'miloszpabis1', 'jebackurwy123')
#     #db.return_data('milonpabis')



