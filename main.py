from fastapi import FastAPI
from uvicorn import run as uvicorn_run

from app.dependencies import (
    Session,
    SessionReadOnly
)


app = FastAPI()

app.dependency_overrides[Session] = Session.create_session
app.dependency_overrides[SessionReadOnly] = SessionReadOnly.create_session


if __name__ == "__main__":
    uvicorn_run(app)
