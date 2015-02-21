import abc

from probability.base import probability_distribution


class DiscreteProbabilityDistribution(probability_distribution.ProbabilityDistribution):
    def get(self, value):
        """
        Returning a probability object.
        :param value: The value of the probability
        :type value: float
        :return: A probability
        :rtype: probability.discrete_probability.base.probability.DiscreteProbability
        """
        return self._get(value)

    @abc.abstractmethod
    def _get(self, value):
        raise NotImplementedError()
