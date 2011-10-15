import couchdb
import settings
import time
#import logging
from django.utils import simplejson

def to_json(python_object):
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}

class CouchClient(object):
    
    def __init__(self):
        self.db = couchdb.Database(settings.DNS_COUCH)
        
    def save(self, doc):
        self.db.save(doc)
        
    def save_feedparser_dict(self, entry, feed):
        del entry["updated_parsed"]
        del entry["published_parsed"]
        entry["type"] = "newsitem"
        entry["feed_url"] = feed.get('id')
        entry["feed"] = {
            'title': feed.get('title'),
            'link':  feed.get('link'),
            'desc': feed.get('subtitle'),
            
        }
        self.save(entry)       