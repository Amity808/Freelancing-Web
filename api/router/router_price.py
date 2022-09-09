from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import oauth
from schemas.gigs import BasicBase, BasicRes
from models.gigs import Basicpackage
from db.database import get_db
from api.repo.repo_price import create_new_basic, list_AllBasic, retrieve_GigId, update_basicId, delete_basicId


router = APIRouter()


@router.post("/create-basicprice")
def create_BasicPrice(basic: BasicBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = create_new_basic(basic, db)
    return price


@router.get("/get-allBasicPrice")
def all_basicprice(db: Session = Depends(get_db)):
    price = list_AllBasic(db)
    return price


@router.get("/basicprice/{id}")
def basicId(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = retrieve_GigId(id, db)
    return price


@router.put("/basicprice/{id}")
def updateId(id: int, basic: BasicBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = update_basicId(id, basic, db)
    return {"Details": "Successfully update the details with the id {id}"}


@router.delete("/basicprice/{id}")
def delete_Id(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    price = delete_basicId(id, db)
    return {"details": f"Suceessfully deleted"}
