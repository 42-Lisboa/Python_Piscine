from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


# ========================== Pydantic BaseModel class =========================
#        Class we use to define the required fields and proper input data
# -----------------------------------------------------------------------------

class StationInfo(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)  # ge(greater than), le(less or equal)
    power_level: float = Field(ge=0, le=100)  # percent | ge(greater or equal)
    oxygen_level: float = Field(ge=0, le=100)  # percent | ge(greater or equal)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200, default=None)


# ============================== Program Test ================================

def main() -> None:
    print("\nSpace Station Data Validation         🪐")
    print("=========================================")

    # 1. Valid Test - Success case
    # ---------------------------------------------------
    print("Success Case:")
    try:
        ok_station = StationInfo(
            station_id="DSS-42",
            name="Lisbon Yellow Station",
            crew_size=15,
            power_level=93.0,  # days on 42 ;)
            oxygen_level=83.5,
            last_maintenance=datetime.now(),
            notes="All systems working properly."
        )
        print(f"ID: {ok_station.station_id}")
        print(f"Name: {ok_station.name}")
        print(f"Crew: {ok_station.crew_size} people")
        print(f"Power: {ok_station.power_level}%")
        print(f"Oxygen: {ok_station.oxygen_level}%")
        print(f"Last maintenance: {ok_station.last_maintenance}")
        print("Status: "
              f"{'Operational' if ok_station.is_operational else 'Offline'}")
        print(f"{ok_station.notes}")
    except ValidationError as e:
        print(f"❌ ValidationError: {e}")

    print("\n=========================================")

    # 2. Invalid Test - Fail case
    # ---------------------------------------------------
    print("Fail Case:")
    try:
        ko_station = StationInfo(
            station_id="DSS-42",
            name="Lisbon Yellow Station",
            crew_size=25,
            power_level=93.0,  # days on 42 ;)
            oxygen_level=83.5,
            last_maintenance=datetime.now(),
            notes="All systems working properly."
        )
        print(f"ID: {ko_station.station_id}")
        print(f"Name: {ko_station.name}")
        print(f"Crew: {ko_station.crew_size} people")
        print(f"Power: {ko_station.power_level}%")
        print(f"Oxygen: {ko_station.oxygen_level}%")
        print(f"Last maintenance: {ko_station.last_maintenance}")
        print("Status: "
              f"{'Operational' if ko_station.is_operational else 'Offline'}")
        print(f"{ko_station.notes}")
    except ValidationError as e:
        print(f"❌ ValidationError: {e}")


if __name__ == "__main__":
    main()
