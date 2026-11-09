from core.packages.base import *
from app.routers.user import router as user_router

app = FastAPI()



app.include_router(user_router)