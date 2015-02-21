Testing
=======
If you read this that mean that you want to do something with the code (probably add or fix).
This README will try to explain how all the tests are organized and how it should look like.

Running
-------
To run the tests that come with probabilities:

1. Install nose (A package for running tests - :command:`pip install nose`).
2. Navigate to the probabilities directory
3. Run :command:`nosetests`.

Guide lines
-----------
Questions about our testing and their answers.

**Q:** What framework we are using?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**A:** We are using the basic unittest that python gives us.
Please don't add anything else like :program:`py.test` and his friends.

**Q:** What do we check?
^^^^^^^^^^^^^^^^^^^^^^^^
**A:** Every object in pymal should be tested with all his function and flows.
Check the returned types and their data.
Tests with mocks as much as able.

**Q:** Where to put my consts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**A:** If they are only for your test put them in your TestCase class.

**Q:** And that's all?
^^^^^^^^^^^^^^^^^^^^^^
**A:** Pretty much yes, but remember to make asserts informative by code or by message.
