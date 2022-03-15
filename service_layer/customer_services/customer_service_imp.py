from entities.customer_class import Customer
from service_layer.customer_services.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):

    def service_create_customer_record(self, customer: Customer) -> Customer:
        pass

    def service_delete_customer_record(self, customer_id: int) -> bool:
        pass
