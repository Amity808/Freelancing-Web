from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import oauth
from schemas.gigs import GigBase,GigRes
from models.gigs import Gig
from db.database import get_db
from api.repo.repo_gigs import create_new_gig, list_allGig, retrieve_Gig_Id, updata_gigId, delete_gigId


router = APIRouter()


@router.post("/create-gig", response_model=GigRes)
def create_gig(gig: GigBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user) ):
    gigs = create_new_gig(gig, db)
    return gigs


@router.get("/get-all-gig")
def get_all(db: Session = Depends(get_db)):
    gigs = list_allGig(db)
    return gigs


@router.get("/get-byId/{id}", response_model=GigRes)
def get_byId(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    gigs = retrieve_Gig_Id(id, db)
    return gigs


@router.put("/update-gig/{id}")
def updateBy_Id(id: int, gig: GigBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    gigs = updata_gigId(id, gig, db)
    return {"Details": "Successfully updated"}


@router.delete("/delete-gig/{id}")
def delete_gigs(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    gigs = delete_gigId(id, db)
    return {"Detail": "Successfully Deleted"}
