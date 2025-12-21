from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey

class client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    document_type: Mapped[str] = mapped_column(String, nullable=False)
    document: Mapped[str] = mapped_column(String, nullable=False)
    emails: Mapped[str] = mapped_column(ForeignKey("emails.id"), nullable=False)
    facilities: Mapped[str] = mapped_column(ForeignKey("facilities.id"), nullable=False)
