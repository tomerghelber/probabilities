from probabilities.discrete_probability.base import probability_distribution
from probabilities.exceptions import GetDiscreteProbabilityValueError

from tests.base.test_probability_distribution import ProbabilityDistributionTest


class DiscreteProbabilityDistributionTest(ProbabilityDistributionTest):
    def setUp(self):
        super().setUp()
        self.super_classes.add(probability_distribution.DiscreteProbabilityDistribution)

    def test_get_not_round(self):
        values = {"1.1", 1.1}

        for value in values:
            with self.assertRaises(GetDiscreteProbabilityValueError) as cm:
                self.tested_object.get(value)

    def test_get_round(self):
        values = {"1.0", 1.0, 1}

        tested_objects = [self.tested_object.get(value) for value in values]

        for tested_object in tested_objects:
            self.assertEqual(tested_objects[0], tested_object)
