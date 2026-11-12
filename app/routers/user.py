from core.packages.routers import *
import app.services.user as service

import app.schema.user as schema

router = APIRouter(
    prefix="/users"
)


@router.get("/me")
def send_user_profile () :
    return "hello user"


@router.post("/get-phone")
def get_user_phone(
    data : schema.SendPhoneDto = Body() , 
    db : Session = Depends(get_db)
) :
    return service.getPhoneService(
        data=data , 
        db = db
    )



@router.post("/verify-phone")
def check_verifycation_code (
    data : schema.CodeDto = Body() ,
    db : Session = Depends(get_db)
) :
    return service.verifyCode(
        data , 
        db
    )



