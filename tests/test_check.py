import pytest
from securepassword import SecurePassword

def test_character_set():
    secpass = SecurePassword()
    # print(secpass.allowed_charcters())
    assert '~' in secpass.allowed_charcters(), 'tilde is allowed'
    assert len(secpass.allowed_charcters()) > 40, 'more than 40 different allowd chars'
