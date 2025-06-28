from pydantic import BaseModel

class PitchIn(BaseModel):
    seller_name: str
    product_name: str
    pitch_text: str
