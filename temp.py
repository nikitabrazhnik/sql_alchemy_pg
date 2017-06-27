

def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


def createlist():
    new_list = []
    for i in 'Nikita Brazhnik':
        new_list.append(i)
    return new_list


if __name__ == '__main__':
    con, meta = connect('postgres','HjkM10wo','imbv1')
    table = meta.tables['users']
    nl = createlist()

    for i in nl:
        statement = table.insert().values(firstname=str(i), lasname=str(i)+'ln', email=nl[0]+'@'+i, pwdhash=str(random.randint(0,10000000)))
        result = con.execute(statement)
