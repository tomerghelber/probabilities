Coding
======

Contents:

.. toctree::
   :maxdepth: 2

   exceptions/index
   discrete/index

Guide lines
-----------
Some basic rules:

1. Tests are in their own directory tree that is equals to the real tree. Never put tests in here! That's why we have a folder for them :)
2. Objects with same interface should inheritance from the same interface.

**Q:** Where do i put a new object?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**A:** Each object should be placed in his own file.

**Q:** Do you have any global files?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**A:** No. This project doesn't seem to need one right now.

Inheritances
------------
All object inheritance the bases class.

Base classes
^^^^^^^^^^^^
.. automodule:: base.probability
.. autoclass:: Probability
   :members:

.. automodule:: base.probability_distribution
.. autoclass:: ProbabilityDistribution
   :members:

Probabilities are separated to two - discrete probability and -TODO: completed the anther one-.
For them we made other base classes:
 - :class:`discrete_probability.base.probability.DiscreteProbability` and :class:`discrete_probability.base.probability_distribution.DiscreteProbabilityDistribution`.
 - TODO: completed the anther one-

