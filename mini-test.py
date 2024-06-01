import pytest
from unittest.mock import patch
import socket
from PortScanD import scan_port

@pytest.fixture
def mock_socket(monkeypatch):
    with patch('socket.socket') as mock_socket_class:
        yield mock_socket_class

def test_port_is_open(mock_socket):
    # Arrange
    mock_socket.return_value.__enter__.return_value.connect.return_value = None
    mock_socket.return_value.__enter__.return_value.getservbyport.return_value = 'http'

    # Act
    result = scan_port('192.168.1.1', 80)

    # Assert
    assert result == '192.168.1.1: Port 80 is open (http).'

def test_port_is_closed(mock_socket):
    # Arrange
    mock_socket.return_value.__enter__.return_value.connect.side_effect = Exception()

    # Act
    result = scan_port('192.168.1.1', 22)

    # Assert
    assert result is None
