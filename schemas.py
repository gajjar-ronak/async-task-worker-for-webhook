from pydantic import BaseModel

class WebhookPayload(BaseModel):
    scope: str
    data: dict