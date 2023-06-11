from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from migrations import User, create_tables


class DBManager:
    def __init__(self, connection_creds):
        self.connection_creds = connection_creds
        self.session = self.init_conn(connection_creds)

    @staticmethod
    def init_conn(conn_creds):
        engine = create_engine(
                "mysql+mysqlconnector://"
                f"{conn_creds['USER']}:"
                f"{conn_creds['PASSWORD']}@{conn_creds['HOST']}:"
                f"{conn_creds['PORT']}")
        session = sessionmaker(
            bind=engine)
        if not create_tables(engine, 'users'):
            print('HZ wtf check db tables existence')
            return
        return session()

    def create_user(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return True

    def check_user_exist(self, user_data):
        user = self.session.query(User).filter(User.user_name == user_data['user_name'])
        return user > 0
