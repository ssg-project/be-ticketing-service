from fastapi import FastAPI, Request
from api.ticket_api import router as ticket_router
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
import logging
import os

# 로거 생성
logger = logging.getLogger("ticketing-service")
logger.setLevel(logging.INFO)


#로깅 핸들러 설정 (중복 방지)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - ticketing-service - %(name)s - %(levelname)s - %(message)s "
        "{pid: %(process)d, tid: %(thread)d}"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

logger.propagate = False  #root logger로 로그 전파 방지



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
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
        log_config=None,  # uvicorn 기본 로깅 비활성화 (root logger 변경 방지)
        log_level="critical"  # uvicorn의 추가 로그 출력을 방지
    )