from tests.base.test_probability.test_init_probability import InitProbabilityTest
from tests.base.test_probability.test_hash_probability import HashProbabilityTest
from tests.base.test_probability.test_arithmetic_probability import ArithmeticProbabilityTest
from tests.base.test_probability.test_booleans_probability import BooleansProbabilityTest


class ProbabilityTest(InitProbabilityTest, HashProbabilityTest, ArithmeticProbabilityTest, BooleansProbabilityTest):
    """
    Base test for probability.
    """
    pass
