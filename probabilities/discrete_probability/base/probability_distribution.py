import abc

from probabilities.base import probability_distribution
from probabilities import exceptions


class DiscreteProbabilityDistribution(probability_distribution.ProbabilityDistribution):
    """Discrete probabilities distribution"""

    def get(self, value):
        """
        Returning a probabilities object.
        :param value: The value of the probabilities
        :type value: float
        :return: A probabilities
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
