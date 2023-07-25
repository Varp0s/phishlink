import threading
import time
from database.database import get_db
from database.crud import add_phishtank_feed
import feeds.feed_source as feed_source

def phish_crawl():
    database = next(get_db())

    phishtank_feed = feed_source.get_phishtank_feed()
    for data in phishtank_feed:
        id = data['phish_id']
        url = data['url']
        add_phishtank_feed(
            id=id,
            url=url,
            db=database
        )

    print("Feeds updated")

    time.sleep(10)
    phish_crawl() 

if __name__ == "__main__":
    threading.Thread(target=phish_crawl).start()
