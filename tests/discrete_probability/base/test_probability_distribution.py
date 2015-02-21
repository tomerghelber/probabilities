from probability.discrete_probability.base import probability_distribution

from tests.base.test_probability_distribution import ProbabilityDistributionTest


class DiscreteProbabilityDistributionTest(ProbabilityDistributionTest):
    def setUp(self):
        super().setUp()
        self.super_classes.add(probability_distribution.DiscreteProbabilityDistribution)
