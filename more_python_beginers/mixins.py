class Loggable:
    def __init__(self):
        self.title = ''

    def log(self):
        print('Log message from '+ self.title)

class Connection:
    def __init__(self):
        self.server = ''

    def connect(self):
        print('Connection to database on '+ self.server)


def framework(item):
    # Perform the connection 
    if isinstance(item, Connection):
        item.connect()

    # Log the operation
    if isinstance(item, Loggable):
        item.log()


class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'


class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just logging'


    
just_log = JustLog()
framework(just_log)
sql_connection = SqlDatabase()
framework(sql_connection)

    

