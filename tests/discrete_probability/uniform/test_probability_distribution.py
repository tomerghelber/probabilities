from unittest import TestCase

from probability.discrete_probability.uniform import probability_distribution
from tests.discrete_probability.base.test_probability_distribution import DiscreteProbabilityDistributionTest


class UniformDiscreteProbabilityDistributionTest(DiscreteProbabilityDistributionTest, TestCase):
    @property
    def _probability_distribution_class(self):
        return probability_distribution.UniformDiscreteProbabilityDistribution

    @property
    def tested_object(self):
        print(1)
        a = self._probability_distribution_class
        print(a)
        b = a()
        print(b)
        return b
