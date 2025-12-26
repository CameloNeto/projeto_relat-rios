from typing import Optional
from enum import Enum
from pydantic import confloat, constr
from .base import ConfiguredBaseModel


class PaymentStatus(str, Enum):
    ABERTO = "Aberto"
    APROVACAO = "Aprovação"
    AGUARDANDO = "Aguardando"
    PAGO = "Pago"
    VENCIDO = "Vencido"
    ARQUIVADO = "Arquivado"
    PARCELADO = "Parcelado"
    NEGATIVADO = "Negativado"


class BillBase(ConfiguredBaseModel):
    due_date: constr(strip_whitespace=True) = None
    payment_status: PaymentStatus
    consumption: confloat(strict=True)
    total_amount_distributor: confloat(strict=True)
    value: confloat(strict=True)
    amount_saved: confloat(strict=True)
    bill_generated: constr(strip_whitespace=True) = None
    facility_id: int

