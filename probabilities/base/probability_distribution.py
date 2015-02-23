import abc
import cmath


class ProbabilityDistribution(abc.ABC):
    """
    :var full: :class:`base.probabilities.Probability` The probabilities 1 of this distribution.
    :var full: :class:`base.probabilities.Probability` The probabilities 0 of this distribution.
    """
    @abc.abstractproperty
    def _probability_class(self):
        """

        :return: The distribution probabilities class
        :rtype: :probabilities.base.probabilities.Probability:
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
        The median of the distribution.

        :return: Median of the distribution.
        :rtype: float
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def variance(self):
        """
        The variance of the distribution.

        :return: Variance of the distribution.
        :rtype: float
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def mode(self):
        """
        The mode of the distribution.

        :return: Mode of the distribution.
        :rtype: float
        """
        raise NotImplementedError()

    @property
    def standard_deviation(self):
        """
        The standard deviation of the distribution.

        :return: Standard deviation of the distribution.
        :rtype: float
        """
        return cmath.sqrt(self.variance)
