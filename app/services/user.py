from core.packages.services import *
from app.database.users import VerifycationCode
import app.schema.user as schema

def getPhoneService (
        data : schema.SendPhoneDto , 
        db : Session
) :
    code = create_random_code()
    verify_code = VerifycationCode(
        code = code ,
        phone = data.phone
    )
    db.add(verify_code)
    db.commit()
    return {
        "result" : "verify code smnt"
    }


def verifyCode (
        data : schema.CodeDto , 
        db : Session
) :
    verify = db.query(VerifycationCode).filter(
        VerifycationCode.code == data.code , 
        VerifycationCode.phone == data.phone
    ).one_or_none()
    if not verify :
        return {
            "result" : "verify not valid"
        }
    return {
        "result" : "verify valid"
    }