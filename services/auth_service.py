from flask import session

class Authentication:
    def __init__(self):
        self.user = 'admin'
        self.password = 'admin'
    
    def login(self, username, password):
        if username == self.user and password == self.password:
            session['username'] = username
            return True
        return False
        
    def logout(self):
        session.pop('username', None)
        return True
    
