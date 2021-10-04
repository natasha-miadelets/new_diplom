import psycopg2


class DB:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'postgres'
        self.password = 'postgres'
        self.dbname = 'postgres'

    def create_connection(self):
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
        return conn

    def user_is_added(self, user_mame: str, cursor):
        query = "SELECT object_repr FROM django_admin_log"
        cursor.execute(query)
        users = cursor.fetchall()

        user_list = list(sum(users, ()))

        for i in user_list:
            if i == user_mame:
                a = []
                a.append(i)
                assert a[0] == user_mame, f'{a[0]} not eq {user_mame}'
