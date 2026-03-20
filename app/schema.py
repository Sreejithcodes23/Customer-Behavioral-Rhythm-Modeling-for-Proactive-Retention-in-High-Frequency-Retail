from pydantic import BaseModel

class NPTInput(BaseModel):
    total_orders: int
    orders_last_30: int
    days_since_last_purchase: float
    total_spend: float
    avg_order_value: float
    spend_last_30: float