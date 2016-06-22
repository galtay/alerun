# alerun | ![travis_img_alt][travis_img]
finds runs in lists of integers

Simply run the file `alerun.py` to see results,

	> python alerun.py

Logs will be generated in a file called `alerun.log` by default.
Unit tests can be run locally by,

	> python tests.py

The module can also be imported and used in other projects,

	> import alerun
	> search_me = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
	> python alerun.find_consecutive_runs(search_me, skip=1, window_size=3)



[travis_img]: https://travis-ci.org/galtay/alerun.svg?branch=master
