import abc

from probability.base import probability
from tests import test_sub_class


class BaseProbabilityTest(test_sub_class.BaseSubClassTest):
    """
    Base test for probability.
    """
    TESTED_PROBABILITY_VALUE = 1 / 3
    BIGGER_PROBABILITY_VALUE = TESTED_PROBABILITY_VALUE * 1.5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.super_classes.add(probability.Probability)

    def setUp(self):
        super().setUp()
        self.tested_probability = self._probability_class(self.TESTED_PROBABILITY_VALUE)
        self.equal_probability = self._probability_class(self.TESTED_PROBABILITY_VALUE)
        self.bigger_probability = self._probability_class(self.BIGGER_PROBABILITY_VALUE)

    @abc.abstractproperty
    def _probability_class(self):
        raise NotImplementedError()

    @property
    def _sub_class(self):
        return self._probability_class
