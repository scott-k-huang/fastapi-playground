import uvicorn
from fastapi import Depends, FastAPI

from app.deps.dependencies import get_token_header
from app.routers import usermanagement

app = FastAPI(dependencies=[Depends(get_token_header)])
app.include_router(usermanagement.router)

@app.get("/")
async def root():
    return {"message": "Hello Complex Applications in new home!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)