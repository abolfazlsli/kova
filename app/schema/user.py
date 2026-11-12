from pydantic import *

class SendPhoneDto(BaseModel) :
    phone : str


class CodeDto(SendPhoneDto) :
    code : int