"""Test includes faker to generate test data"""
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

# pylint: disable=unnecessary-dunder-call, invalid-name

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for Calculator and Calculation tests"""
    operation_mapping = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mapping.keys()))
        operation_func = operation_mapping[operation_name]

        # Ensure b is not zero for divide operation to prevent ZeroDivisionError
        if operation_func is divide and b == Decimal('0'):
            b = Decimal('1')

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Allows pytest to recognize --num_record argument"""
    parser.addoption("--num_record", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Dynamically generate test cases based on command-line argument"""
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_record")  # Fixed argument name

        # Generate test cases
        parameters = list(generate_test_data(num_records))

        # Adjust parameters to fit test function expectations
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]

        metafunc.parametrize("a, b, operation, expected", modified_parameters)
