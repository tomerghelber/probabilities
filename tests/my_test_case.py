from unittest.util import safe_repr


class MyTestCase(object):
    def assertIsSubClass(self, sub_class, super_class):
        """Same as self.assertTrue(issubclass(sub_class, super_class)), with a nicer default message."""
        if not issubclass(sub_class, super_class):
            standardMsg = '%s is not a subclass of %r' % (safe_repr(sub_class), super_class)
            self.fail(self._formatMessage(sub_class, standardMsg))
