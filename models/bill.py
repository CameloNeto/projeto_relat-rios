from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, Float, CheckConstraint

class bill(Base):
    __tablename__ = "bills"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    due_: Mapped[String] = mapped_column(String, nullable=True)
    payment_status: Mapped[String] = mapped_column(String, nullable=False)
    consumption: Mapped[Float] = mapped_column(Float, nullable=False)
    total_amount_distributor: Mapped[Float] = mapped_column(Float, nullable=False)
    value: Mapped[Float] = mapped_column(Float, nullable=False)
    amount_saved: Mapped[Float] = mapped_column(Float, nullable=False)
    bill_generated: Mapped[String] = mapped_column(String, nullable=True)
    facility_id: Mapped[ForeignKey] = mapped_column(ForeignKey("facilities.id"))

    __table_args__ = (
        CheckConstraint(
            "payment_status IN ('Aberto', 'Aprovação', 'Aguardando', 'Pago', 'Vencido', 'Arquivado', 'Parcelado', 'Negativado')",
            "payment_status"
        ),
    )