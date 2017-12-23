import unittest

from . import (
    test_sentence,
)  # noqa:


loader = unittest.TestLoader()
suite = unittest.TestSuite((
    loader.loadTestsFromModule(test_sentence),  # type: ignore
))
