from pydantic import BaseModel

### ticket
class ReserveTicketRequest(BaseModel):
    concert_id: int
    # user_id: int