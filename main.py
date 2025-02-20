from fastapi import FastAPI
from api.ticket_api import router as ticket_router
from starlette.middleware.cors import CORSMiddleware
#from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

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
app.include_router(ticket_router, prefix="/api/v1", tags=["ticket"])

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

#Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8002, reload=True)