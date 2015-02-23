from probability.discrete_probability.uniform import probability
from probability.discrete_probability.base import probability_distribution


class UniformDiscreteProbabilityDistribution(probability_distribution.DiscreteProbabilityDistribution):

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    @property
    def _probability_class(self):
        return probability.UniformDiscreteProbability

    @property
    def expected_value(self):
        return 1 / (self.b - self.a)

    @property
    def median(self):
        return (self.b + self.a) / 2.0

    @property
    def mode(self):
        return self.expected_value

    @property
    def variance(self):
        return 0

    def _get(self, value):
        if self.a < value < self.b:
            return self._probability_class(self.expected_value)
        return self._probability_class(0)

    def __repr__(self):
        return "X~U({0:d}, {0:d})".format(self.a, self.b)
