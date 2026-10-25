# test_chainpurge.py
"""
Tests for ChainPurge module.
"""

import unittest
from chainpurge import ChainPurge

class TestChainPurge(unittest.TestCase):
    """Test cases for ChainPurge class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainPurge()
        self.assertIsInstance(instance, ChainPurge)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainPurge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
