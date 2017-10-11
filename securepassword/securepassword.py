import string
import secret
import re

class SecurePassword:

    _default_length = 8
    _special_characters = "[ !#$%&'()*+,-./[\\\]^_`{|}~"
    _default_character_set = string.ascii_letters + string.digits + _special_characters
    _character_set = None

    def __init__(self,
                 character_set = _default_character_set):
        self._character_set = character_set

    def allowed_charcters(self):
        return self._character_set

    def check_password_quality(self, password):
        error_text = ''
        ea = []
        if len(password) < 8:
            ea.append('password too short')
        if not re.search(r"\d", password):
            ea.append('password has to contain a number')
        if not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~", password):
            ea.append('password has to contain a special character')
        if not re.search(r"[A-Z]", password):
            ea.append('password has to contain an upper case letter')
        if not re.search(r"[a-z]", password):
            ea.append('password has to contain a lower case letter')

        error_text = '; '.join(ea)
        return error_text


