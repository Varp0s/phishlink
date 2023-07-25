import uvicorn
import threading
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import PhishTankFeed
from fisher.fisher import phish_crawl
import config as conf

app = FastAPI()

@app.get("/")
def root_dir():
    return {"sitemap": "/phishtank"}

def get_feed(db: Session, model):
    feeds = db.query(model).all()
    return feeds

@app.get("/phishtank")
def get_phishtank_feed(db: Session = Depends(get_db)):
    return get_feed(db, PhishTankFeed)  

def crawl_thread():
    thread = threading.Thread(target=phish_crawl)
    thread.start()

if __name__ == "__main__":
    crawl_thread()  
    uvicorn.run(app, host=conf.HOST, port=conf.PORT)
