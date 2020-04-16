"""
Module dedicated to secured data

It will rely on the external package cryptography
"""

import os
import base64
import uuid

# Internal key used for the token generation in the URL (during the sharing)
KEY = 'bAvGUC_7oazo4cIeNBt8t23bPe3Hvq8livGqQxSV-z0='


class PyCrypto(object):
  class __internal(object):
    _props, _context, jsOnLoadEvtsFnc = {}, {}, []

  def __init__(self, src=None):
    self.__src = src if src else self.__internal()

  def encrypt(self, data, token=None, salt=None):
    """
    This function will use the cryptography to ensure a secured encryption of the different credential and private data.
    This can be also used to protect data from the report.
    In order to ensure the right privacy please do not store the token and the salt in the framework.

    example

    Documentation

    :param data: The data to be encrypted
    :param token: Optional. The token used to encrypt the data
    :param salt: Optional. The salt id

    :return: The encrypted data with the salt used
    """
    from cryptography.fernet import Fernet
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    if token is None:
      # used for the URL generation
      return Fernet(KEY).encrypt(data.encode())

    salt = salt if salt is not None else os.urandom(32)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    if hasattr(token, 'encode'):
      encrypted_key = base64.urlsafe_b64encode(kdf.derive(bytes(token.encode('utf-8'))))
    else:
      encrypted_key = token
    return Fernet(encrypted_key).encrypt(bytes(data.encode('latin1'))).decode('latin1'), salt.decode('latin1')

  def decrypt(self, encrypted, token=None, salt=None, label=''):
    """
    This function will use the two keys in order to decrypt the data.
    In case of failure this function will raise an exception.

    Example
    PyCrypto().decrypt(encrypted)

    Documentation

    :param encrypted: The encrypted data
    :param token: Optional. The token used to encrypt the data
    :param salt: Optional. The salt id
    :param label: Optional. A label used to store the reference in the log file

    :return: A string with the decrypted data
    """
    from cryptography.fernet import Fernet
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    if token is None:
      # used for the URL generation
      return Fernet(KEY).decrypt(encrypted)

    if hasattr(self.__src, 'log'):
      # In the admin section the report is not defined
      self.__src.log("SECURITY|%s|%s|password decoding" % (self.__src.run.current_user, label))
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=bytes(salt.encode('latin1')), iterations=100000, backend=default_backend())
    if hasattr(token, 'encode'):
      encrypted_key = base64.urlsafe_b64encode(kdf.derive(bytes(token.encode('utf-8'))))
    else:
      encrypted_key = token
    return Fernet(encrypted_key).decrypt(bytes(encrypted.encode('latin1'))).decode('utf-8')

  @property
  def getId(self):
    """
    Return a unique token

    Example
    PyCrypto.getId

    Related Pages:

			https://docs.python.org/2/library/uuid.html

    :return: A unique ID (based on the timestamp
    """
    return uuid.uuid4()

  @property
  def key(self):
    """
    Return a Fernet key

    Example
    PyCrypto().key

    Related Pages:

			https://cryptography.io/en/latest/fernet/
    """
    from cryptography.fernet import Fernet
    return Fernet.generate_key()

  @classmethod
  def b64encode(cls, text, salt=None):
    """

    Example
    PyCrypto.b64encode("Test")

    Related Pages:

			https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/

    :param text: The text to be encrypted
    :param salt: Optional. The salt used for the encryption (default None)

    :return:
    """
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    salt = salt if salt is not None else os.urandom(32)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(bytes(text.encode('latin1'))))

  @classmethod
  def cryptKeyPairs(cls, msg, key1, key2):
    """

    Example

    Documentation

    :param msg:
    :param key1:
    :param key2:
    :return:
    """
    from cryptography.fernet import Fernet, MultiFernet
    f = MultiFernet([Fernet(key1), Fernet(key2)])
    return f.encrypt(bytes(msg.encode('latin1')))

  @classmethod
  def decryptKeyPairs(cls, encrypted, key1, key2):
    """

    Example

    Documentation

    :param encrypted: The encrypted data
    :param key1:
    :param key2:
    :return:
    """
    from cryptography.fernet import Fernet, MultiFernet
    f = MultiFernet([Fernet(key1), Fernet(key2)])
    return f.decrypt(bytes(encrypted.encode('latin1')))

