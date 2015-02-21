import abc


class ProbabilityDistribution(abc.ABC):
    @abc.abstractproperty
    def _probability_class(self):
        """

        :return: The distribution probability class
        :rtype: :probability.base.probability.Probability:
        """
        raise NotImplementedError()

    def __init__(self):
        self.full = self._probability_class(1)
        self.zero = -self.full
