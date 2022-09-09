from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core import oauth
from schemas.profile import ProfileBase, ProfileRes

from db.database import get_db
from api.repo.repo_profile import create_new_profile, retrieve_ProfileId, list_AllProfile, update_ProfileId, delete_ProfileId


router = APIRouter()


@router.post("/create-profile")
def create_profile(profile: ProfileBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    profiles = create_new_profile(profile, db)
    return profiles


@router.get("/get-all-profile")
def all_profile(db: Session = Depends(get_db)):
    profiles = list_AllProfile(db)
    return profiles


@router.get("/get-profile/{id}")
def standardId(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    profiles = retrieve_ProfileId(id, db)
    return profiles


@router.put("/update-profile/{id}")
def updateId(id: int, profile: ProfileBase, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    profiles = update_ProfileId(id, profile, db)
    return {"Details": "Successfully update the details with the id {id}"}


@router.delete("/delete-profile/{id}")
def delete_Id(id: int, db: Session = Depends(get_db), current_user=Depends(oauth.get_current_user)):
    profiles = delete_ProfileId(id, db)
    return {"details": f"Suceessfully deleted"}

