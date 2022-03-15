from custom_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.customer_class import Customer

customer_dao = CustomerDAOImp()

def test_create_customer_success():
    customer = Customer(0,"first","last")
    result = customer_dao.create_customer_record(customer)
    assert result.customer_id != 0

def test_create_customer_with_malformed_id():
    # if the wrong data type of id is provided in the customer object the method should still work
    customer = Customer("one", "bad","id")
    result = customer_dao.create_customer_record()
    assert result.customer_id != 0

def test_delete_customer_success():
    result = customer_dao.delete_customer_record(-1)
    assert result

def test_no_customer_to_delete():
    #catch no customer is deleted by the method
    try:
        customer_dao.delete_customer_record(-1000)
        assert False
    except NothingDeleted as e:
        assert str(e) == "There was no customer with the given Id"