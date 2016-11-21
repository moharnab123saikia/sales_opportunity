from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Sentiment(Model):
    id = Column(Integer, primary_key=True)
    phone = Column(String(50), unique = True, nullable=False)
    sound = Column(Float)
    fingerprint = Column(Float)
    color = Column(Float)
    headphone = Column(Float)
    design = Column(Float)
    size = Column(Float)
    network = Column(Float)
    battery = Column(Float)
    camera = Column(Float)
    safety= Column(Float)
    memory= Column(Float)
    intelligence= Column(Float)
    performance= Column(Float)
    assistant= Column(Float)


    def __repr__(self):
        return self.phone
