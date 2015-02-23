class ProbabilityError(ArithmeticError):
    """
    Thrown when can't calculate any probabilities.
    """
    pass


class ProbabilityValueError(ValueError):
    """
    Thrown when probabilities value is wrong.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ProbabilityInitValueError(ProbabilityValueError):
    """
    Thrown when probabilities is not between 0 to 1.
    """
    ERROR_COMMENT = "Probability is between 0 to 1"

    def __init__(self):
        super().__init__(self.ERROR_COMMENT)


class GetDiscreteProbabilityValueError(ProbabilityValueError):
    """
    Thrown when requested probabilities is not right.
    """
    ERROR_COMMENT = " Discrete must be round"

    def __init__(self):
        super().__init__(self.ERROR_COMMENT)

