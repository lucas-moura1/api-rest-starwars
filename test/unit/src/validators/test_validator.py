import unittest

from src.validators.validator import *
from src.errors import RequestError


class TestValidator(unittest.TestCase):

    def test_should_raise_none_body(self) -> None:
        body = None

        self.assertRaises(RequestError, validate_body_existence, body)

    def test_should_raise_field_existence(self) -> None:
        body = {}
        field_name = 'name'

        self.assertRaises(RequestError, validate_field_existence, body, field_name)


if __name__ == '__main__':
    unittest.main()
