from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, BigInteger, Boolean
from sqlalchemy.orm import relationship

__author__ = 'Tahir'

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True)
    active = Column(Boolean, default=False)
    otp = Column(String(20))
    user_id = Column(BigInteger)

    


# , unique=True