from fastapi import FastAPI
from api.user_api import router as user_router
from api.ticket_api import router as ticket_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# middleware 설정
app.add_middleware( # cors middleware
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router 설정
app.include_router(user_router, prefix="/api/v1", tags=["user"])
app.include_router(ticket_router, prefix="/api/v1", tags=["ticket"])

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
