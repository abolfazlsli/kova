from core.packages.database import *



class User(BasicTabale) : 
    __tablename__ = "user"



class VerifycationCode (BasicTabale) :
    __tablename__ = "veifycation_code"
    code = Column(Integer , nullable=False)
    phone = Column(String , nullable=False)