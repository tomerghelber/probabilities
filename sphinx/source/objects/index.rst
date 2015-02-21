Coding
======

Contents:

.. toctree::
   :maxdepth: 2

   exceptions/index

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
