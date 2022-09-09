from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import oauth
from schemas.gigs import StandardBase, StandardRes

from db.database import get_db
from api.repo.repo_standard import create_new_standard, list_AllStandard, retrieve_standardId, update_standardId, delete_standardId


router = APIRouter()


@router.post("/create-StandardPrice")
def create_StandardPrice(standard: StandardBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = create_new_standard(standard, db)
    return price


@router.get("/get-allStandardPrice")
def all_standardprice(db: Session = Depends(get_db)):
    price = list_AllStandard(db)
    return price


@router.get("/standardprice/{id}")
def standardId(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = retrieve_standardId(id, db)
    return price


@router.put("/standardprice/{id}")
def updateId(id: int, standard: StandardBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = update_standardId(id, standard, db)
    return {"Details": "Successfully update the details with the id {id}"}


@router.delete("/standardprice/{id}")
def delete_Id(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = delete_standardId(id, db)
    return {"details": f"Suceessfully deleted"}

