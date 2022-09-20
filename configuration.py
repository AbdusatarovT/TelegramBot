POSTGRES = {
    'user': 'tahir',
    'pw': '1',
    'db': 'db_bot',
    'host': 'localhost',
    'port': '5432',
}
  
SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
BOT_TOKEN = '5642913997:AAEmWF6vM6QXwBEY58EFw2r_gpi9-H1q_xM'
