import hashlib
class User(object):


    def __init__(self, first_name, last_name, email_address, username=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.username = username
        self._password_hash = None

    def __repr__(self):
        """Returns the attributes (excluding password) of the user as a string"""
        return '{}, {}, {}, {}'.format(self.first_name, self.last_name, self.email_address, self.username)

    @property
    def password_hash(self):
        """Get the current hashed password. If no password is set then the default is None"""
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        """
        Takes a password and converts it to a hashed value and assigns it to the _password property
            :param password: password entered
            :type password: string
        """
        self._password_hash = hashlib.sha256(str.encode(password)).hexdigest()

    def check_password(self, password):
            """
            Takes a string password and checks that is matches the assigned hash.
                :param password: password entered
                :type password: string
                :return: True if the password matches, otherwise False
                :rtype: bool
             """
            password_hash = hashlib.sha256(str.encode(password)).hexdigest()
            return password_hash == self._password_hash
