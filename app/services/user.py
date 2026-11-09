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
    return code