from tests.base.test_probability.base_test_probability import BaseProbabilityTest


class HashProbabilityTest(BaseProbabilityTest):
    """
    Base test for probability hash.
    """

    def test__hash__same_instance(self):
        self.assertEqual(hash(self.tested_probability), hash(self.tested_probability))

    def test__hash_equals(self):
        self.assertNotEqual(hash(self.tested_probability), hash(self.equal_probability))

    def test__hash_not_equals(self):
        self.assertNotEqual(hash(self.tested_probability), hash(self.bigger_probability))
