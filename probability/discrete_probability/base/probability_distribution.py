import abc

from probability.base import probability_distribution
from probability import exceptions


class DiscreteProbabilityDistribution(probability_distribution.ProbabilityDistribution):
    """Discrete probability distribution"""

    def get(self, value):
        """
        Returning a probability object.
        :param value: The value of the probability
        :type value: float
        :return: A probability
        :rtype: probability.discrete_probability.base.probability.DiscreteProbability
        :raise exceptions.ProbabilityValueError
        """
        value = float(value)
        if not value.is_integer():
            raise exceptions.GetDiscreteProbabilityValueError()
        return self._get(value)

    @abc.abstractmethod
    def _get(self, value):
        raise NotImplementedError()
