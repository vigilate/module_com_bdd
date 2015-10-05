from sqlalchemy import engine, exc

class vigilate_db:
    """VIGILATE's dabatase communication module"""

    def __init__(self):
        self.connected = False

        self.connect("mysql+pymysql", "root", "toor")
        if not self.connected:
            self.connect("postgres", "root", "toor")

    def connect(self, dbtype, user, password, dbname="vigilate", host="localhost"):
        try:
            self.e = engine.create_engine("%s://%s:%s@%s/%s" % (dbtype, user, password, host, dbname))
            connection = self.e.connect()
        except exc.OperationalError as err:
            print (err)
        else:
            print ("Successfully connected to the %s database." % dbtype)
            self.connected = True

