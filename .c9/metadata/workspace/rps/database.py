{"filter":false,"title":"database.py","tooltip":"/rps/database.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":40,"column":32},"action":"remove","lines":["from sqlalchemy import create_engine","from sqlalchemy.orm import sessionmaker","from sqlalchemy.ext.declarative import declarative_base","","from blog import app","","engine = create_engine(app.config[\"SQLALCHEMY_DATABASE_URI\"])","Base = declarative_base()","Session = sessionmaker(bind=engine)","session = Session()","","import datetime","","from sqlalchemy import Column, Integer, String, Text, DateTime","from .database import Base, engine","from flask.ext.login import UserMixin","","from sqlalchemy import ForeignKey","from sqlalchemy.orm import relationship","","class User(Base, UserMixin):","    __tablename__ = \"users\"","","    id = Column(Integer, primary_key=True)","    name = Column(String(128))","    email = Column(String(128), unique=True)","    password = Column(String(128))","    entries = relationship(\"Entry\", backref=\"author\")","","class Entry(Base):","    __tablename__ = \"entries\"","","    id = Column(Integer, primary_key=True)","    title = Column(String(1024))","    content = Column(Text)","    datetime = Column(DateTime, default=datetime.datetime.now)","    author_id = Column(Integer, ForeignKey('users.id'))","    ","","","Base.metadata.create_all(engine)"],"id":77},{"start":{"row":0,"column":0},"end":{"row":32,"column":32},"action":"insert","lines":["from sqlalchemy import create_engine","from sqlalchemy.orm import sessionmaker","from sqlalchemy.ext.declarative import declarative_base","","from blog import app","","engine = create_engine(app.config[\"SQLALCHEMY_DATABASE_URI\"])","Base = declarative_base()","Session = sessionmaker(bind=engine)","session = Session()","","from sqlalchemy import Column, Integer, String, Text, DateTime","from .database import Base, engine","","from sqlalchemy import ForeignKey","from sqlalchemy.orm import relationship","","class Player1(Base):","    __tablename__ = \"playerone\"","","    id = Column(Integer, primary_key=True)","    move = Column(String(128))","","","class Player2(Base):","    __tablename__ = \"playertwo\"","","    id = Column(Integer, primary_key=True)","    move = Column(String(128))","    ","","","Base.metadata.create_all(engine)"]}]]},"ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":31,"column":0},"end":{"row":31,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":15,"state":"start","mode":"ace/mode/python"}},"timestamp":1450553864764,"hash":"ab4a56aea0d2daabb19b19d27c507e5d49bd0481"}