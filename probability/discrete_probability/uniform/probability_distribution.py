from probability.discrete_probability.uniform import probability
from probability.discrete_probability.base import probability_distribution


class UniformDiscreteProbabilityDistribution(probability_distribution.DiscreteProbabilityDistribution):
    @property
    def _probability_class(self):
        return probability.UniformDiscreteProbability

    def _get(self, value):
        return self._probability_class(value)
