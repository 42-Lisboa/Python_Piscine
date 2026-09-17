from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional


# =============================== Enum class ==================================
#         Class we use to define a fixed set of allowed constant values
# -----------------------------------------------------------------------------

class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


# ========================== Pydantic BaseModel class =========================
#        Class we use to define the required fields and proper input data
# -----------------------------------------------------------------------------

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = False

    @model_validator(mode='after')
    def id_validator(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with \"AC\" (Alien Contact)")
        return self  # return 'self' to demonstrate success validation

    @model_validator(mode='after')
    def physical_validator(self):
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def telepathic_validator(self):
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode='after')
    def strong_signals_validator(self):
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


# ============================== Program Test ================================

def main() -> None:
    print("\nAlien Contact Log Validation         👽")
    print("=========================================")

    # 1. Valid Test - Success case
    # ---------------------------------------------------
    print("Success Case:")
    try:
        ok_contact = AlienContact(
            contact_id="AC_2020_042",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(f"ID: {ok_contact.contact_id}")
        print(f"Type: {ok_contact.contact_type.value}")
        print(f"Location: {ok_contact.location}")
        print(f"Signal: {ok_contact.signal_strength}/10")
        print(f"Duration: {ok_contact.duration_minutes} minutes")
        print(f"Witnesses: {ok_contact.witness_count}")
        print(
            f"Message: '{ok_contact.message_received}'"
            if ok_contact.message_received
            else "Message: None"
        )
    except ValidationError as e:
        print(f"❌ ValidationError: {e}")

    print("\n=========================================")

    print("\nFail Case: Incorrect contact_id")
    print("-------------------------------------------------------")
    try:
        ko_contact = AlienContact(
            contact_id="XC_2020_042",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(f"This won't be reached: {ko_contact.contact_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}")

    print("\nFail Case: Not verified Physical contact")
    print("-------------------------------------------------------")
    try:
        ko_contact = AlienContact(
            contact_id="AC_2020_042",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.PHYSICAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print(f"This won't be reached: {ko_contact.contact_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}")

    print("\nFail Case: Improper Telepathic contact")
    print("-------------------------------------------------------")
    try:
        ko_contact = AlienContact(
            contact_id="AC_2020_042",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(f"This won't be reached: {ko_contact.contact_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}")

    print("\nFail Case: Strong signal without message")
    print("-------------------------------------------------------")
    try:
        ko_contact = AlienContact(
            contact_id="AC_2020_042",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.VISUAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            is_verified=True
        )
        print(f"This won't be reached: {ko_contact.contact_id}")
    except ValidationError as e:
        clean_e = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(f"❌ ValidationError: {clean_e}\n")


if __name__ == "__main__":
    main()
