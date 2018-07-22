# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ynab_client
from ynab_client.api.categories_api import CategoriesApi  # noqa: E501
from ynab_client.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = ynab_client.api.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_categories(self):
        """Test case for get_categories

        List categories  # noqa: E501
        """
        pass

    def test_get_category_by_id(self):
        """Test case for get_category_by_id

        Single category  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
