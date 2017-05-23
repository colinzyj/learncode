# encoding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
import gconf
connect = 'mysql+mysqldb://' + gconf.DB_USER + ':' + gconf.DB_PASSWD + '@' +\
          gconf.DB_HOST + ':' + str(gconf.DB_PORT) + '/' + gconf.DB_NAME
engine = create_engine(connect, encoding='utf8', echo=False)
Base = declarative_base()


class User(Base):
    __tablename__ = 'testuser'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    fullname = Column(String(32))
    password = Column(String(32))

    # def __repr__(self):
    #     return "<User(name ='%s', fullname='%s', password='%s')>" \
    #            % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)
ed_user = User(name='colin', fullname='colinfn', password='123456')
print ed_user.name
print ed_user.fullname
Session = sessionmaker(bind=engine)
session = Session()
# session.add(ed_user)
# session.add_all([
#     User(name='colin2', fullname='colinfn', password='123456'),
#     User(name='colin3', fullname='colinfn', password='123456')
# ])
# # our_user = session.query(User).filter_by(name='ed').first()
session.commit()
print session.query(User).count()