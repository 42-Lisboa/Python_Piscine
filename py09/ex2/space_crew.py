from enum import Enum
from datetime import datetime
from pydantic import (  # type: ignore
    BaseModel,
    Field,
    model_validator,
    ValidationError)


# =============================== Enum class ==================================
#         Class we use to define a fixed set of allowed constant values
# -----------------------------------------------------------------------------

class Rank(Enum):
    COMMANDER = "commander"
    CAPTAIN = "captain"
    LIEUTENANT = "lieutenant"
    OFFICER = "officer"
    CADET = "cadet"


# ========================== Pydantic BaseModel class =========================
#        Class we use to define the required fields and proper input data
# -----------------------------------------------------------------------------

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def id_validator(self):
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with \"M\"")
        return self

    @model_validator(mode='after')
    def command_validator(self):
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                return self
        else:
            raise ValueError("Must have at least one Commander or Captain")

    @model_validator(mode='after')
    def experience_validator(self):
        if self.duration_days <= 365:
            return self
        half_crew = len(self.crew) / 2
        experienced_crew = 0
        for member in self.crew:
            if member.years_experience >= 5:
                experienced_crew += 1
        if experienced_crew < half_crew:
            raise ValueError("Long missions (> 365 days) "
                             "need 50% experienced crew (5+ years)")
        else:
            return self

    @model_validator(mode='after')
    def active_validator(self):
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} "
                                 "is not active and cannot launch")
        return self


# ============================== Program Test ================================

def main() -> None:
    print("\nSpace Mission Crew Validation          🚀")
    print("=========================================")

    # 1. Valid Test - Success case
    # ---------------------------------------------------
    print("Success Case:")
    try:
        ok_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="SC-001", name="Sarah Connor",
                    rank=Rank.COMMANDER, age=45,
                    specialization="Mission Command", years_experience=15,
                    is_active=True
                ),
                CrewMember(
                    member_id="JS-002", name="John Smith",
                    rank=Rank.LIEUTENANT, age=32,
                    specialization="Navigation", years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ-003", name="Alice Johnson",
                    rank=Rank.OFFICER, age=28,
                    specialization="Engineering", years_experience=4,
                    is_active=True
                )
            ],
            budget_millions=2500.0
        )
        print(f"Mission: {ok_mission.mission_name}")
        print(f"ID: {ok_mission.mission_id}")
        print(f"Destination: {ok_mission.destination}")
        print(f"Duration: {ok_mission.duration_days} days")
        print(f"Budget: ${ok_mission.budget_millions}M")
        print(f"Crew size: {len(ok_mission.crew)}")
        print("Crew members:")
        for m in ok_mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}")

    print("\n=========================================")

    print("\nFail Case: Missing Commander or Captain")
    print("-------------------------------------------------------")
    try:
        ko_mission = SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Moon Base Expansion",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=100,
            crew=[
                CrewMember(
                    member_id="JS-002", name="John Smith",
                    rank=Rank.LIEUTENANT, age=32,
                    specialization="Navigation", years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ-003", name="Alice Johnson",
                    rank=Rank.OFFICER, age=28,
                    specialization="Engineering", years_experience=4,
                    is_active=True
                )
            ],
            budget_millions=500.0
        )
        print(f"This won't be reached: {ko_mission.mission_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}")

    print("\nFail Case: Not enough experienced crew for long mission")
    print("-------------------------------------------------------")
    try:
        ko_mission_exp = SpaceMission(
            mission_id="M2025_PLUTO",
            mission_name="Pluto Base Exploration",
            destination="Pluto",
            launch_date=datetime.now(),
            duration_days=500,
            crew=[
                CrewMember(
                    member_id="JD-001", name="Jane Doe",
                    rank=Rank.COMMANDER, age=40,
                    specialization="Mission Command", years_experience=4,
                    is_active=True
                ),
                CrewMember(
                    member_id="BS-002", name="Bob Smith",
                    rank=Rank.OFFICER, age=25,
                    specialization="Science", years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ-003", name="Alice Johnson",
                    rank=Rank.OFFICER, age=28,
                    specialization="Engineering", years_experience=4,
                    is_active=True
                )
            ],
            budget_millions=1500.0
        )
        print(f"This won't be reached: {ko_mission_exp.mission_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}")

    print("\nFail Case: Inactive crew member assigned")
    print("-------------------------------------------------------")
    try:
        ko_mission_act = SpaceMission(
            mission_id="M2025_VENUS",
            mission_name="Venus Surface Probe",
            destination="Venus",
            launch_date=datetime.now(),
            duration_days=100,
            crew=[
                CrewMember(
                    member_id="JD-001", name="Jane Doe",
                    rank=Rank.COMMANDER, age=40,
                    specialization="Command", years_experience=15,
                    is_active=True
                ),
                CrewMember(
                    member_id="TR-003", name="Tom Riddle",
                    rank=Rank.CADET, age=22,
                    specialization="Trainee", years_experience=1,
                    is_active=False
                )
            ],
            budget_millions=800.0
        )
        print(f"This won't be reached: {ko_mission_act.mission_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}\n")


if __name__ == "__main__":
    main()
