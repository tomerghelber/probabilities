import abc

from tests.my_test_case import MyTestCase


class BaseSubClassTest(abc.ABC, MyTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.super_classes = set()

    def setUp(self):
        pass

    @abc.abstractproperty
    def _sub_class(self):
        raise NotImplementedError()

    def test_sub_class(self):
        for super_class in self.super_classes:
            self.assertIsSubClass(self._sub_class, super_class)
