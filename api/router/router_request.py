from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import oauth
from schemas.gigs import RequestBase, RequestRes
from models.gigs import Basicpackage
from db.database import get_db
from api.repo.repo_request import create_new_request, list_AllRequest, \
    retrieve_RequestId, update_RequestId, delete_RequestId


router = APIRouter()


@router.post("/create-request")
def create_Request(request: RequestBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    requests = create_new_request(request, db)
    return requests


@router.get("/get-allrequest")
def all_request(db: Session = Depends(get_db)):
    requests = list_AllRequest(db)
    return requests


@router.get("/get-request/{id}")
def requestId(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    requests = retrieve_RequestId(id, db)
    return requests


@router.put("/request/{id}")
def updateId(id: int, request: RequestBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    requests = update_RequestId(id, request, db)
    return {"Details": "Successfully update the details with the id {id}"}


@router.delete("/request/{id}")
def delete_Id(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    requests = delete_RequestId(id, db)
    return {"details": f"Suceessfully deleted"}
