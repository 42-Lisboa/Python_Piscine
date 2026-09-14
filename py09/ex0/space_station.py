from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class StationInfo(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)  # ge(greater than), le(less or equal)
    power_level: float = Field(ge=0, le=100)  # percent
    oxygen_level: float = Field(ge=0, le=100)  # percent
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=10, default=None)
