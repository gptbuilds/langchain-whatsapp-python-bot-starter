from fastapi import APIRouter, Request, Depends
from src.app.services.ping import ping
from src.app.exceptions import generic_exception_handler

router = APIRouter()

router.get("/ping")(ping)
