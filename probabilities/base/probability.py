import abc
import hashlib
import os

from probabilities import exceptions


class Probability(abc.ABC):
    """
    """

    FULL = 1

    def __init__(self, probability: float or int, not_probability=None):
        """
        :param probability: The probabilities value. Must be between 0 to 1
        :type probability: float or int
        :param not_probability: Using to create the opposite probabilities.
        :type not_probability: Probability or None
        """
        probability = float(probability)
        if probability < 0 or probability > 1:
            raise exceptions.ProbabilityInitValueError()

        b = hashlib.md5()
        b.update(os.urandom(24))
        b.update(str(probability).encode())
        self.__hash = int(b.hexdigest(), 16)

        self.__probability = probability
        self._not = Probability(self.FULL - probability, self) if not_probability is None else not_probability

        self._cut = dict([(self, self), ])
        self._union = dict([(self, self), ])

    # --- Getters ---

    # @abc.abstractmethod
    # def intersection(self, other_probability):
    # """
    # Returns the intersection of self with other_probability.
    #
    #     :param other_probability: The probabilities to intersect with.
    #     :type other_probability: Probability
    #     :return: The intersections the probabilities.
    #     :rtype: Probability
    #     """
    #     raise NotImplementedError()
    #
    # @abc.abstractmethod
    # def union(self, other_probability):
    #     """
    #     Returns the union of self with other_probability.
    #
    #     :param other_probability: The probabilities to union with.
    #     :type other_probability: Probability
    #     :return: The union of the probabilities.
    #     :rtype: Probability
    #     """
    #     raise NotImplementedError()
    #
    # # --- Adders ---
    #
    # @abc.abstractmethod
    # def add_intersection(self, other_probability, result_probability):
    #     """
    #     Adding an intersection of self with other_probability
    #
    #     :param other_probability: The probabilities to intersect with.
    #     :type other_probability: Probability
    #     :param result_probability: The intersected probabilities.
    #     :type result_probability: Probability
    #     """
    #     raise NotImplementedError()
    #
    # @abc.abstractmethod
    # def add_union(self, other_probability, result_probability):
    #     """
    #     Adding an union of self with other_probability
    #
    #     :param other_probability: The probabilities to union with.
    #     :type other_probability: Probability
    #     :param result_probability: The union probabilities.
    #     :type result_probability: Probability
    #     """
    #     raise NotImplementedError()

    # --- Arithmetic ---

    def __float__(self):
        return self.__probability

    def __neg__(self):
        return self._not

    # --- Booleans ---

    def __eq__(self, other):
        return float(other) == float(self)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return self < other or self == other

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return self > other or self == other

    # --- Other ---
    def __repr__(self):
        return "<{class_name:s} {value:f}>".format(
            class_name=self.__class__.__name__,
            value=float(self)
        )

    def __hash__(self):
        return self.__hash
