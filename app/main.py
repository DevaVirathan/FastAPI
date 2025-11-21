from fastapi import FastAPI
from app.routes.user_route import router as user_router
from app.routes.migrate_route import router as migrate_router


app = FastAPI(title="FastAPI MySQL Backend")


app.include_router(user_router)
app.include_router(migrate_router)