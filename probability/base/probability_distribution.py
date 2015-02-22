import abc
import cmath


class ProbabilityDistribution(abc.ABC):
    """
    :var full: :class:`base.probability.Probability` The probability 1 of this distribution.
    :var full: :class:`base.probability.Probability` The probability 0 of this distribution.
    """
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

    @abc.abstractproperty
    def expected_value(self):
        """
        The expected value of the distribution.

        :return: The expected value of the distribution.
        :rtype: float
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def median(self):
        """
        The Median of the distribution.

        :return: Median of the distribution.
        :rtype: float
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def variance(self):
        raise NotImplementedError()

    @abc.abstractproperty
    def mode(self):
        raise NotImplementedError()

    @property
    def standard_deviation(self):
        return cmath.sqrt(self.variance)
