import os
# from app import app
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv
#
# load_dotenv()
#
#
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
# db = SQLAlchemy(app)


# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     intro = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"<Article {self.id}"