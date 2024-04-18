from fastapi import FastAPI

from routers.user import router as user_router

app = FastAPI(
    debug=True,
    title='UserDTO Test Task'
)
app.include_router(user_router)
