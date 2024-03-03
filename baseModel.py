from pydantic import BaseModel

class KeyValueStore(BaseModel):
    key: str
    value: str