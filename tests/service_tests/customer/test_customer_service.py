from custom_exceptions.bad_customer_info import BadCustomerInfo
from data_access_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.customer_class import Customer
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

"""
create service tests
"""


def test_catch_non_string_first_name():
    try:
        customer = Customer(0, 40, "this is fine")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "customer information is poorly formatted, please try again"


def test_catch_non_string_last_name():
    try:
        customer = Customer(0, "this is fine", 40)
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "customer information is poorly formatted, please try again"


def test_first_name_too_long():
    try:
        customer = Customer(0, "this string is too long for our method", "this is fine")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "customer information is poorly formatted, please try again"


def test_last_name_too_long():
    try:
        customer = Customer(0, "this is fine", "this is fine if you allow names over 20 characters long")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "customer information is poorly formatted, please try again"


"""
delete service tests
"""


def test_catch_non_typcastable_id():
    try:
        customer_service.service_delete_customer_record("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "customer information is poorly formatted, please try again"
