import psycopg2


class DB:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'postgres'
        self.password = 'postgres'
        self.dbname = 'postgres'
        self.conn = psycopg2.connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

    def user_is_added(self, user_mame: str):
        query = "SELECT object_repr FROM django_admin_log"
        self.cursor.execute(query)
        users = self.cursor.fetchall()

        user_list = list(sum(users, ()))

        for i in user_list:
            if i == user_mame:
                a = []
                a.append(i)
                assert a[0] == user_mame, f'{a[0]} not eq {user_mame}'

    def close_cursor(self):
        self.conn.close()
