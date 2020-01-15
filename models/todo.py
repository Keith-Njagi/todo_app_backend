from app import db, ma
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __repr__(self):
        return '<Todo %r>' % self.title

    def insert_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.order_by(cls.id.desc()).all()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod #TODO: read on keyword functions & default functions
    def update_todo(cls, id, title=None, description=None, updated=None): #update
        record = cls.fetch_by_id(id)
        if title:
            record.title = title
        if description:
            record.description = description
        if updated:
            record.updated = updated

        db.session.commit()
        return True

    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True

class TodoSchema(ma.Schema):
    class Meta:
        # fields we want to expose
        fields = ('id', 'title', 'description', 'created', 'updated')