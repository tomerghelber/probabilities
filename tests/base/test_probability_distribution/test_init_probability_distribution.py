from probability.base.probability import Probability
from tests.base.test_probability_distribution import base_test_probability_distribution


class InitProbabilityDistributionTest(base_test_probability_distribution.BaseProbabilityDistributionTest):
    def test__init__full_value(self):
        self.assertEqual(Probability.FULL, float(self.tested_object.full))

    def test__init__zero_value(self):
        self.assertEqual(Probability.FULL - Probability.FULL, float(self.tested_object.zero))

    def test__init__zero_not_full(self):
        self.assertEqual(self.tested_object.zero, -self.tested_object.full)
