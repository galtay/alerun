"""Test the alerun module"""

import unittest
import alerun

class TestGenWindow(unittest.TestCase):
    """Test _gen_window."""

    def test_correct_behaviour(self):
        """Assert we get window entries"""
        seq = [1, 2, 3, 4]
        window_size = 3
        expected = [(1, 2, 3), (2, 3, 4)]
        actual = []
        for maybe_run in alerun._gen_window(seq, window_size):
            actual.append(maybe_run)
        self.assertEqual(actual, expected)


class TestIsMonoSkip(unittest.TestCase):
    """Test _is_mono_skip."""

    def test_positive(self):
        """Assert all entries = skip returns True"""
        diffs = [3, 3, 3]
        skip = 3
        actual = alerun._is_mono_skip(diffs, skip)
        self.assertTrue(actual)

    def test_negative(self):
        """Assert all entries = -skip returns True"""
        diffs = [-3, -3, -3]
        skip = 3
        actual = alerun._is_mono_skip(diffs, skip)
        self.assertTrue(actual)

    def test_mixed(self):
        """Assert mixed case of skip and -skip returns False"""
        diffs = [-3, 3, -3]
        skip = 3
        actual = alerun._is_mono_skip(diffs, skip)
        self.assertFalse(actual)

    def test_not_skip(self):
        """Assert mixed case of skip and -skip returns False"""
        diffs = [-3, -5, -3]
        skip = 3
        actual = alerun._is_mono_skip(diffs, skip)
        self.assertFalse(actual)

    def test_empty_diffs(self):
        """Assert empty diffs raises exception"""
        diffs = []
        skip = 3
        with self.assertRaises(Exception):
            alerun._is_mono_skip(diffs, skip)


class TestFindConsecutiveRuns(unittest.TestCase):
    """Test find_consecutive_runs."""

    def test_provided_example(self):
        """Assert correct behaviour for provided example."""
        search_me = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
        expected = [0, 4, 6, 7]
        actual = alerun.find_consecutive_runs(search_me, skip=1, window_size=3)
        self.assertEqual(actual, expected)

    def test_window_too_small(self):
        """Assert exception on window size < 1."""
        search_me = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
        with self.assertRaises(Exception):
            alerun.find_consecutive_runs(search_me, skip=1, window_size=1)

    def test_one_run_doesnt_fit(self):
        """Assert return None for window size > input size."""
        search_me = [1, 2]
        expected = None
        actual = alerun.find_consecutive_runs(search_me, skip=1, window_size=3)
        self.assertEqual(actual, expected)

    def test_no_runs(self):
        """Assert return None for no runs found."""
        search_me = [1, -1, 2, -2, 3, -3, 4, -4]
        expected = None
        actual = alerun.find_consecutive_runs(search_me, skip=1, window_size=3)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
