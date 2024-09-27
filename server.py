from fastapi import FastAPI
import uvicorn
from games.keno import Keno
from games.limbo import Limbo
import db

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{username}")
async def get_user(username: str):
    return db.get_user(username)

if __name__ == "__main__":

    app.include_router(Keno.router)
    app.include_router(Limbo.router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
