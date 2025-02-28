from fastapi import FastAPI, Request
from api.ticket_api import router as ticket_router
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
import logging
import os

# Kubernetes 환경에서 파드 및 노드 정보 가져오기
pod_name = os.environ.get("POD_NAME", "unknown-pod")
node_name = os.environ.get("NODE_NAME", "unknown-node")


# 로거 생성
logger = logging.getLogger("ticketing-service")
logger.setLevel(logging.INFO)




# 중복 핸들러 방지
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s "
        f"{{pod: {pod_name}, node: {node_name}}}"  # pod_name, node_name 직접 추가
    )
    handler.setFormatter(formatter)
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
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
        log_config=None,  # Uvicorn 기본 로깅 비활성화
        log_level="info"  # 기존의 "critical" 대신 "info" 유지
    )