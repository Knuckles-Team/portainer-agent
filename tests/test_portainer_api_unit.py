import unittest
from unittest.mock import MagicMock, patch
from portainer_agent.portainer_api import PortainerApi

class TestPortainerApiUnit(unittest.TestCase):
    @patch('requests.Session')
    def setUp(self, mock_session_class):
        self.mock_session = mock_session_class.return_value
        # Mock system status check in __init__
        mock_response = MagicMock()
        mock_response.status_code = 200
        self.mock_session.get.return_value = mock_response
        self.api = PortainerApi(base_url="http://test", token="test-token")
        self.mock_session.get.reset_mock() # Reset after init check

    def test_create_container_with_name(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Id": "123"}
        self.mock_session.post.return_value = mock_response

        config = {"Image": "nginx"}
        result = self.api.create_container(endpoint_id=1, config=config, name="my-container")

        self.mock_session.post.assert_called_once()
        args, kwargs = self.mock_session.post.call_args
        self.assertEqual(kwargs['params'], {"name": "my-container"})
        self.assertEqual(kwargs['json'], config)
        self.assertEqual(result, {"Id": "123"})

    def test_stop_container_with_timeout(self):
        mock_response = MagicMock()
        mock_response.status_code = 204
        self.mock_session.post.return_value = mock_response

        self.api.stop_container(endpoint_id=1, container_id="123", timeout=30)

        self.mock_session.post.assert_called_once()
        args, kwargs = self.mock_session.post.call_args
        self.assertEqual(kwargs['params'], {"t": 30})
        self.assertIsNone(kwargs.get('json'))

    def test_restart_container_with_timeout(self):
        mock_response = MagicMock()
        mock_response.status_code = 204
        self.mock_session.post.return_value = mock_response

        self.api.restart_container(endpoint_id=1, container_id="123", timeout=10)

        self.mock_session.post.assert_called_once()
        args, kwargs = self.mock_session.post.call_args
        self.assertEqual(kwargs['params'], {"t": 10})

if __name__ == '__main__':
    unittest.main()
