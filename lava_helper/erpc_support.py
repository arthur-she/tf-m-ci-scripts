# erpc_support.py - eRPC support module for TF-M LAVA CI
"""
eRPC support module for TF-M LAVA CI infrastructure.
This module extends the existing LAVA helper functionality to support eRPC testing.
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

logger = logging.getLogger(__name__)


class eRPCConfig:
    """Configuration class for eRPC testing parameters"""
    
    # Default eRPC configurations for supported platforms
    PLATFORM_CONFIGS = {
        'musca_b1': {
            'erpc_enabled': True,
            'erpc_mode': 'uart',
            'erpc_uart_device': '/dev/ttyUSB0',
            'erpc_uart_baudrate': 115200,
            'erpc_client_binary': 'tfm_erpc_client',
            'erpc_test_timeout': 1800,
            'erpc_connection_timeout': 60,
            'erpc_ns_only': True
        },
        'musca_s1': {
            'erpc_enabled': True,
            'erpc_mode': 'uart',
            'erpc_uart_device': '/dev/ttyUSB0',
            'erpc_uart_baudrate': 115200,
            'erpc_client_binary': 'tfm_erpc_client',
            'erpc_test_timeout': 1800,
            'erpc_connection_timeout': 60,
            'erpc_ns_only': True
        },
        'mps2/an521': {
            'erpc_enabled': True,
            'erpc_mode': 'tcp',
            'erpc_tcp_host': 'localhost',
            'erpc_tcp_port': 5555,
            'erpc_client_binary': 'tfm_erpc_client',
            'erpc_test_timeout': 1800,
            'erpc_connection_timeout': 60,
            'erpc_ns_only': True,
            'erpc_fvp_params': [
                '-C', 'mps2_board.erpc.enable=1',
                '-C', 'mps2_board.erpc.port=5555'
            ]
        }
    }
    
    @classmethod
    def get_platform_config(cls, platform: str) -> Dict[str, Any]:
        """Get eRPC configuration for a specific platform"""
        return cls.PLATFORM_CONFIGS.get(platform, {})
    
    @classmethod
    def is_erpc_supported(cls, platform: str) -> bool:
        """Check if platform supports eRPC testing"""
        return platform in cls.PLATFORM_CONFIGS
