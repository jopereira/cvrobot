
from setuptools import setup

if __name__ == '__main__':
    setup(name='cvrobot',
          author='Jose Orlando Pereira',
          author_email='jop@di.uminho.pt',
          description='cienciavitae.pt API',
          version='0.1.0',
          install_requires=['selenium', 'getpass', 'keyring'],
          packages=['cvrobot']) 
