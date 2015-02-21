class ProbabilityError(ArithmeticError):
    """
    Thrown when can't calculate any probability.
    """
    pass


class ProbabilityValueError(ValueError):
    """
    Thrown when probability is not between 0 to 1
    """
    ERROR_COMMENT = "Probability is between 0 to 1"

    def __init__(self):
        super().__init__(self.ERROR_COMMENT)
