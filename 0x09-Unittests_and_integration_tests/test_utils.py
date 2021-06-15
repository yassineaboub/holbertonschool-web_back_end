#!/usr/bin/env python3
"""test module
"""


import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """generic test of utilities
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """return the supposed to return
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """test raise a keyError
        """
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)
            self.assertEqual(raises.exception.message, exception)


class TestGetJson(unittest.TestCase):
    """return json form URL
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test the expected json return
        """
        mock_get = Mock()
        mock_get.json.return_value = test_payload
        with patch('requests.get', return_value=mock_get):
            response = get_json(test_url)
            mock_get.json.assert_called_once()
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """memoization test
    """
    def test_memoize(self):
        """memo test
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            memo = TestClass()
            memo.a_property
            memo.a_property
            mock.assert_called_once()
