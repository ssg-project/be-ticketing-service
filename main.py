from fastapi import FastAPI
from api.ticket_api import router as ticket_router
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
import logging

# 로거 생성
logger = logging.getLogger("ticketing-service")
logger.setLevel(logging.INFO)


# 로깅 설정
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - ticketing-service - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()]
# )

handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - ticketing-service - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

# 기존 핸들러 제거 후 새로운 핸들러 추가 (중복 방지)
if not logger.hasHandlers():
    logger.addHandler(handler)


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

Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8002, reload=True)