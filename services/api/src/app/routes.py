from fastapi import APIRouter, Request, Depends
from app.models import Message
from app.services.ping import ping
from app.exceptions import generic_exception_handler

router = APIRouter()

router.get("/ping")(ping)
router.add_exception_handler(Exception, generic_exception_handler)

