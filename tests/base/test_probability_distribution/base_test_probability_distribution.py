import abc

from probability.base import probability_distribution
from tests import test_sub_class


class BaseProbabilityDistributionTest(test_sub_class.BaseSubClassTest):
    def setUp(self):
        super().setUp()
        self.super_classes.add(probability_distribution.ProbabilityDistribution)

    @abc.abstractproperty
    def _probability_distribution_class(self):
        raise NotImplementedError()

    @abc.abstractproperty
    def tested_object(self):
        raise NotImplementedError()

    @property
    def _sub_class(self):
        return self._probability_distribution_class
