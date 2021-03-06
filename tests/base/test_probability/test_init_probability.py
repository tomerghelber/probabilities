from probabilities import exceptions
from tests.base.test_probability.base_test_probability import BaseProbabilityTest


class InitProbabilityTest(BaseProbabilityTest):
    """
    Base test for probabilities init.
    """

    def test__init__lower_than_0(self):
        with self.assertRaises(exceptions.ProbabilityInitValueError):
            self._probability_class(-0.1)

    def test__init__greater_than_1(self):
        with self.assertRaises(exceptions.ProbabilityInitValueError):
            self._probability_class(1.1)
