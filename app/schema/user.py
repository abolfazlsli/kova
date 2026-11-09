from pydantic import *

class SendPhoneDto(BaseModel) :
    phone : str