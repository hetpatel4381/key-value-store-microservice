from fastapi import FastAPI, HTTPException
from baseModel import KeyValueStore

app = FastAPI()

key_value_store = {}

@app.get("/")
async def get_home_detail():
    return {"message":"Hello World !"}

@app.post("/set/")
async def set_key_value(key_value: KeyValueStore):
    key_value_store[key_value.key] = key_value.key
    return {"message": "Key-Value pair stored successfully !"}

@app.get("/get/{key}")
async def get_value(key: str):
    value = key_value_store.get(key)
    if value is not None:
        return {"Key": key, "Value": value}
    else:
        raise HTTPException(status_code=404, detail="Key not found !")

@app.delete("/delete/{key}")
async def delete_key(key: str):
    try:
        del key_value_store[key]
        return {"message": f"Key {key} deleted Successfully !"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Key not found !")
    
if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port="8000")