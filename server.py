from fastapi import FastAPI
import uvicorn
from games.keno import Keno
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    app.include_router(Keno.router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
