import pytest
from PortScanD import *


def test_scan_port():
    assert scan_port('1.1.1.1', 53) == '1.1.1.1: Port 53 is open (domain).'