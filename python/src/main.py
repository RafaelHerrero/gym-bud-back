from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users_routes

app = FastAPI(title="Gym-Bud-back App")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    users_routes.router,
    prefix="/users",
    tags=["rota users"],
    )

@app.get("/", tags=["Home Page"])
async def root():
    return {'api ok home page'}

@app.get("/ops/live", tags=["Home Page"])
async def ops_live():
    return 200

@app.get("/ops/ready", tags=["Home Page"])
async def ops_ready():
    return 200
