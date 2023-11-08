"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test calc app"""

    def test_add(self):
        """Test add function"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtract function"""
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6)
