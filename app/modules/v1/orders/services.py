from core.schemas import CommonsDependencies
from core.services import BaseServices
from db.engine import app_engine

from . import models, schemas
from .config import settings
from .crud import OrdersCRUD


class OrderServices(BaseServices):
    def __init__(self, service_name: str, crud: OrdersCRUD = None) -> None:
        super().__init__(service_name, crud)

    async def create(self, data: schemas.CreateRequest, commons: CommonsDependencies) -> dict:
        # Calculate tax rate, vat amount, and total amount
        order = {}
        order["amount"] = 0
        order["discount_amount"] = 0
        order["vat_amount"] = 0
        order["total_amount"] = 0
        order["tax_rate"] = settings.vat

        for order_item in data["order_items"]:
            order["amount"] += order_item["price"] * order_item["quantity"]
        order["vat_amount"] = order["amount"] * order["tax_rate"]
        order["total_amount"] = order["amount"] + order["vat_amount"]

        order["status"] = "pending"
        order["created_by"] = self.get_current_user(commons=commons)
        order["created_at"] = self.get_current_datetime()
        data_save = models.Orders(**order).model_dump()
        return await self.save(data=data_save)

    async def active(self, order_id: str, commons: CommonsDependencies) -> dict:
        data = {}
        data["status"] = "active"
        data["updated_by"] = self.get_current_user(commons=commons)
        data["updated_at"] = self.get_current_datetime()
        return await self.update_by_id(_id=order_id, data=data)


order_crud = OrdersCRUD(database_engine=app_engine, collection="orders")
order_services = OrderServices(service_name="orders", crud=order_crud)
