# “Let's define a function that connects to a database:
# we want to connect to a default database by simply calling this function with no parameters.
# We also want to connect to any other database by passing to the function the appropriate parameters”


def connect(**options):
    conn_params = {
        'host':options.get('host', '127.0.0.1'),
        'port':options.get('port', 5432),
        'user':options.get('user', ''),
        'pwd':options.get('pwd', '')
        
    }
    print(conn_params)

connect()
connect(host = '127.0.0.42',port = 5433)
connect(port = 5431, user = 'fab', pwd = 'gandalf')