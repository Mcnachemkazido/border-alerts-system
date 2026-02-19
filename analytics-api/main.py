import uvicorn
from fastapi import FastAPI
from routes import route
app = FastAPI()

app.include_router(route)


if __name__ == "__main__":
    uvicorn.run(app,port=8000,host="localhost")
