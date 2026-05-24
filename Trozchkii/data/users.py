from sqlalchemy import Column, Integer, Boolean, String, DateTime
from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Баллы за каждый тест (0–20)
    revolution_vs_tradition_score = Column(Integer, default=0)
    libertad_vs_fascismo_score = Column(Integer, default=0)
    monarchy_vs_theocracy_score = Column(Integer, default=0)

    # Флаги: пройден ли тест? (True/False)
    revolution_vs_tradition = Column(Boolean, default=False)
    libertad_vs_fascismo = Column(Boolean, default=False)
    monarchy_vs_theocracy = Column(Boolean, default=False)

    last_test_date = Column(DateTime)
