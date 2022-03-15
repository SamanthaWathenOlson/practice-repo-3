from data_access_layer.customer_dal.customer_dao_interface import CustomerDAOInterface
from entities.customer_class import Customer


class CustomerDAOImp(CustomerDAOInterface):

    def create_customer_record(self, customer: Customer) -> Customer:
        sql = "insert into customers values(default, %s, %s"

    def delete_customer_record(self, customer_id: int) -> bool:
        pass
