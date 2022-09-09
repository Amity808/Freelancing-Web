from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.database import get_db
from models.gigs import Gig
from models.users import Users

router = APIRouter(include_in_schema=False)

templates = Jinja2Templates(directory="templates")


@router.get('/')
def gig_home(request: Request, db: Session = Depends(get_db), msg: str = None):
    gigs = db.query(Gig).all()
    return templates.TemplateResponse("gig_homepage.html", {"request": request, "gigs": gigs, "msg": msg})