import unittest

from probability.discrete_probability.uniform import probability
from tests.discrete_probability.base.test_probability import DiscreteProbabilityTest


class UniformDiscreteProbabilityTest(DiscreteProbabilityTest, unittest.TestCase):
    """
    Discrete probability
    """

    @property
    def _probability_class(self):
        return probability.UniformDiscreteProbability
