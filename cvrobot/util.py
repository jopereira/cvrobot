import getpass
import keyring

def pedePassword(user):
    passwd = keyring.get_password("cvrobot", user)
    if passwd == None:
        passwd = getpass.getpass()
        keyring.set_password("cvrobot", user, passwd)
    else:
        print("Password found in keyring.")
    return passwd
