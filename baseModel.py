from pydantic import BaseModel

class KeyValueStore(BaseModel):
    key: str
    value: str

class UpdateKeyValue(BaseModel):
    new_value: str