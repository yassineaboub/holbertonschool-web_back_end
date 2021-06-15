#!/usr/bin/env python3
"""test module
"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, param
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Map"""

    @parameterized.expand([
        param(1, nested_map={"a": 1}, path=("a",)),
        param({"b": 2}, nested_map={"a": {"b": 2}}, path=("a",)),
        param(2, nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(self, expected, nested_map, path):
        """utils.access_nested_map test"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        param(KeyError, nested_map={}, path=("a",)),
        param(KeyError, nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, expected, nested_map, path):
        """utils.access_nested_map test"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """get json"""

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """utils.get_json test"""
        mock_object = Mock()
        mock_object.json.return_value = test_payload

        with unittest.mock.patch('utils.requests.get',
                                 return_value=mock_object):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Memoize test"""

    def test_memoize(self):
        """memoize test method"""

        class TestClass:
            """Class testing"""

            def a_method(self):
                """a_method method"""
                return 42

            @memoize
            def a_property(self):
                """a_property method"""
                return self.a_method()

        with unittest.mock.patch.object(TestClass,
                                        'a_method',
                                        return_value=42) as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()
