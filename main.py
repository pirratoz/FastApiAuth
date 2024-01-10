from fastapi import FastAPI
from uvicorn import run as uvicorn_run


app = FastAPI()


if __name__ == "__main__":
    uvicorn_run(app)
