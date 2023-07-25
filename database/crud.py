from sqlalchemy.orm import Session
from .models import PhishTankFeed
from .database import get_db

def add_feed(db: Session, model, **kwargs):
    feed = db.query(model).filter_by(**kwargs).first()

    if feed:
        for key, value in kwargs.items():
            setattr(feed, key, value)
        db.commit()
        db.refresh(feed)
        return feed
    else:
        new_feed = model(**kwargs)
        db.add(new_feed)
        db.commit()
        db.refresh(new_feed)
        return new_feed

def add_phishtank_feed(db: Session, id: int, url: str):
    return add_feed(db, PhishTankFeed, id=id, url=url)
