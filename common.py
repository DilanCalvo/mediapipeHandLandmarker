"""Common module for shared state and variables.

This module contains global variables used across different modules
to share hand detection results and timestamps.
"""

from settings import *

# Global variable to store the latest hand detection result
detection_result = None

# Global variable to store the timestamp of the latest detection
detection_timestamp = 0

