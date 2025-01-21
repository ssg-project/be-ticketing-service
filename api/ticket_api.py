from fastapi import APIRouter, Depends, HTTPException, Request
from redis import Redis
from sqlalchemy.orm import Session
from services.ticket_service import TicketService
from dto.dto import *

router = APIRouter(prefix='/ticket', tags=['ticket'])

@router.post("/reserve", description='')
async def reserve_ticket(
    request: Request,
    request_body: ReserveTicketRequest,
):
    try:
        ticket_service = TicketService()

        result = await ticket_service.reserve_ticket(
            request_body.user_id, 
            request_body.concert_id
        )

        print(result)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))