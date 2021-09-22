# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrderController(BaseTestCase):
    """OrderController integration test stubs"""

    def test_create_order(self):
        """Test case for create_order

        crete order
        """
        order = None
        response = self.client.open(
            '/v1/order',
            method='POST',
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
