from probabilities.base import probability
from tests.base.test_probability.base_test_probability import BaseProbabilityTest


class ArithmeticProbabilityTest(BaseProbabilityTest):
    """
    Base test for probabilities arithmetic.
    """

    def test__float__value(self):
        self.assertEqual(self.TESTED_PROBABILITY_VALUE, float(self.tested_probability))

    def test__neg__(self):
        self.assertEqual(self.tested_probability._not, -self.tested_probability)

    def test__neg__value(self):
        self.assertEqual(probability.Probability.FULL - float(self.tested_probability), float(-self.tested_probability))
