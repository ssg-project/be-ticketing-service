from fastapi import APIRouter, Depends, HTTPException, Request
from services.ticket_service import TicketService
from dto.dto import *
import json

router = APIRouter(prefix='/ticket', tags=['ticket'])

@router.post("/reserve", description='')
async def reserve_ticket(
    request: Request,
    request_body: ReserveTicketRequest,
):
    current_user = await get_current_user(request)
    
    try:
        ticket_service = TicketService()

        result = await ticket_service.reserve_ticket(
            # request_body.user_id,
            current_user["user_id"],
            request_body.concert_id
        )

        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def get_current_user(request: Request):
    scope_data = request.headers.get("X-Scope")

    if not scope_data:
        raise HTTPException(status_code=401, detail="인증되지 않은 요청입니다.")
    try:
        scope = json.loads(scope_data)
        user = scope.get("user")
        if not user or not user.get('is_authenticated'):
            raise HTTPException(status_code=401, detail="인증되지 않은 요청입니다.")
        return user
    except:
        raise HTTPException(status_code=401, detail="인증되지 않은 요청입니다.")