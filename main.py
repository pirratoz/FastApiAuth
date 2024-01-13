from fastapi import FastAPI
from uvicorn import run as uvicorn_run

from app.dependencies import (
    Session,
    SessionReadOnly,
    DatabaseConnector,
    IsAuth,
)
from app.docs import Tags
from app.routers import users


def setup_dependency(app: FastAPI, db: DatabaseConnector) -> None:
    app.dependency_overrides[Session] = db.get_session
    app.dependency_overrides[SessionReadOnly] = db.get_session_read_only
    app.dependency_overrides[IsAuth] = IsAuth.auth


def include_routers(app: FastAPI) -> None:
    app.include_router(users, tags=[Tags.users])


def main() -> None:
    app = FastAPI()
    db = DatabaseConnector()

    setup_dependency(app, db)
    include_routers(app)
    
    uvicorn_run(app)


if __name__ == "__main__":
    main()
