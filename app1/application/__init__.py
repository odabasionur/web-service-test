from flask import Flask

print('APP1 INIT & __name__ :', __name__)
app = Flask('__main__')

from application import endpoints

