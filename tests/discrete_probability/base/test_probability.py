from probability.discrete_probability.base import probability
from tests.base.test_probability import ProbabilityTest


class DiscreteProbabilityTest(ProbabilityTest):
    """
    Discrete probability base test.
    """

    def setUp(self):
        super().setUp()
        self.super_classes.add(probability.DiscreteProbability)
