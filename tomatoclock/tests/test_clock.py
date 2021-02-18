import pytest
from tomatoclock.clock import Timer


class TestTimer:
    def setup(self):
        self.timer = Timer()

    def test_set_second(self):
        self.timer.set_second(5)
        assert self.timer._second == 5

    def test_set_minute(self):
        self.timer.set_minute(5)
        assert self.timer._minute == 5
        