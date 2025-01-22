from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

### ticket
class ReserveTicketRequest(BaseModel):
    concert_id: int
    # user_id: int