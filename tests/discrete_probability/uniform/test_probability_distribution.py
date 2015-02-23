from unittest import TestCase

from probability.discrete_probability.uniform import probability_distribution
from tests.discrete_probability.base.test_probability_distribution import DiscreteProbabilityDistributionTest


class UniformDiscreteProbabilityDistributionTest(DiscreteProbabilityDistributionTest, TestCase):
    @property
    def _probability_distribution_class(self):
        return probability_distribution.UniformDiscreteProbabilityDistribution

    @property
    def tested_object(self):
        a = self._probability_distribution_class
        b = self._probability_distribution_class(1, 2)
        return b
