from fastapi import FastAPI

from routers import router as user_router
from database import init_models

app = FastAPI(
    debug=True,
    title='UserDTO Test Task'
)
app.include_router(user_router)
