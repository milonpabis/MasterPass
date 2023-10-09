from gui import LoginPage, QApplication, Passwords

#todo
# - complete register mode
# - connect database to register mode
# - dynamic loading of saved passwords
# - style improvement

if __name__ == "__main__":
    app = QApplication()
    window = Passwords()
    app.exec()
