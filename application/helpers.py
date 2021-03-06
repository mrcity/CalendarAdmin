from application import app, authomatic
from flask.ext.login import current_user

# encrypt and decrypt
from Crypto.Cipher import AES
from Crypto import Random

# is_safe_url
from urlparse import urlparse, urljoin
from flask import request, url_for, session

# http://flask.pocoo.org/snippets/62/
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

# encrypt_string & decrypt_string: used to encrypt url so users can't guess eachother URL		   
#TODO: This was a bad idea, it can be incremented easily and past URLs work after the request is deleted. It needs to be combined with the user ID + row_id at least.
#		Usually a separate database is used to keep track of the encoded URLS, this allows a random string to be used.
#		I wanted to avoid this because Heroku charges you when your database goes over like 10k rows.
def encrypt_string(value):
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(app.config['ENCRYPTION_KEY'], AES.MODE_CFB, iv)
	msg = iv + cipher.encrypt(bytes(value))
	return msg.encode("hex")

def decrypt_string(value):
	try:
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(app.config['ENCRYPTION_KEY'], AES.MODE_CFB, iv)
		return cipher.decrypt(value.decode("hex"))[len(iv):]
	except:
		return False
		
def credentials(name='credentials'):
	# if you're getting keyerrors here, you need to check is_valid_credentials and redirect to login with next=request.url
	return authomatic.credentials(session[name]) 
	
def is_valid_credentials(name='credentials'):
	return current_user.is_authenticated() and session.get(name) and credentials(name).valid