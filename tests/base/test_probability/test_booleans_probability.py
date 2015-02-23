from tests.base.test_probability.base_test_probability import BaseProbabilityTest


class BooleansProbabilityTest(BaseProbabilityTest):
    """
    Base test for probabilities booleans.
    """

    def test__eq__other_probability(self):
        self.assertEqual(self.tested_probability, self.equal_probability)

    def test__eq__value(self):
        self.assertEqual(self.tested_probability, self.TESTED_PROBABILITY_VALUE)

    def test_value__eq__(self):
        self.assertEqual(self.TESTED_PROBABILITY_VALUE, self.tested_probability)

    def test__lt__other_probability(self):
        self.assertLess(self.tested_probability, self.bigger_probability)

    def test__lt__value(self):
        self.assertLess(self.tested_probability, self.BIGGER_PROBABILITY_VALUE)

    def test_value__lt__(self):
        self.assertLess(self.TESTED_PROBABILITY_VALUE, self.bigger_probability)

    def test__le__other_probability(self):
        self.assertLessEqual(self.tested_probability, self.equal_probability)
        self.assertLessEqual(self.tested_probability, self.bigger_probability)

    def test__le__value(self):
        self.assertLessEqual(self.tested_probability, self.TESTED_PROBABILITY_VALUE)
        self.assertLessEqual(self.tested_probability, self.BIGGER_PROBABILITY_VALUE)

    def test_value__le__(self):
        self.assertLessEqual(self.TESTED_PROBABILITY_VALUE, self.tested_probability)
        self.assertLessEqual(self.TESTED_PROBABILITY_VALUE, self.bigger_probability)

    def test__ne__other_probability(self):
        self.assertNotEqual(self.tested_probability, self.bigger_probability)

    def test__ne__value(self):
        self.assertNotEqual(self.tested_probability, self.BIGGER_PROBABILITY_VALUE)

    def test_value__ne__(self):
        self.assertNotEqual(self.BIGGER_PROBABILITY_VALUE, self.tested_probability)

    def test__gt__other_probability(self):
        self.assertGreater(self.bigger_probability, self.tested_probability)

    def test__gt__value(self):
        self.assertGreater(self.BIGGER_PROBABILITY_VALUE, self.tested_probability)

    def test_value__gt__(self):
        self.assertGreater(self.bigger_probability, self.TESTED_PROBABILITY_VALUE)

    def test__ge__other_probability(self):
        self.assertGreaterEqual(self.equal_probability, self.tested_probability)
        self.assertGreaterEqual(self.bigger_probability, self.tested_probability)

    def test__ge__value(self):
        self.assertGreaterEqual(self.TESTED_PROBABILITY_VALUE, self.tested_probability)
        self.assertGreaterEqual(self.BIGGER_PROBABILITY_VALUE, self.tested_probability)

    def test_value__ge__(self):
        self.assertGreaterEqual(self.tested_probability, self.TESTED_PROBABILITY_VALUE)
        self.assertGreaterEqual(self.bigger_probability, self.TESTED_PROBABILITY_VALUE)
