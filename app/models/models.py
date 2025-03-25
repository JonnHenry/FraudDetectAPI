from typing import Any, Dict, Optional
from pydantic import BaseModel
import pandas as pd

class PredictionInput(BaseModel):
    income: float
    name_email_similarity: Optional[float]
    prev_address_months_count: int
    current_address_months_count: int
    customer_age: int
    days_since_request: Optional[float]
    intended_balcon_amount: Optional[float]
    payment_type: str
    zip_count_4w: Optional[int]
    velocity_6h: Optional[float]
    velocity_24h: Optional[float]
    velocity_4w: Optional[float]
    bank_branch_count_8w: Optional[int]
    date_of_birth_distinct_emails_4w: int
    employment_status: str
    credit_risk_score: float
    email_is_free: int
    housing_status: str
    phone_home_valid: Optional[int]
    phone_mobile_valid: Optional[int]
    bank_months_count: int
    has_other_cards: int
    proposed_credit_limit: float
    foreign_request: Optional[int]
    source: Optional[str]
    session_length_in_minutes: Optional[float]
    device_os: str
    keep_alive_session: Optional[int]
    device_distinct_emails_8w: Optional[int]
    device_fraud_count: Optional[int]
    month: int

    def to_dataframe(self) -> pd.DataFrame:
        """Convierte la instancia en un DataFrame de Pandas"""
        return pd.DataFrame([self.model_dump()])


class PredictionOutput(BaseModel):
    prediction: bool

class Message_Error(BaseModel):
    status_code: int
    detail: Any
    headers: Optional[Dict[str, str]]