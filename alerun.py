"""
Module that provides run finding in lists.

Problem description,

Write a python function named "find_consecutive_runs" that accepts as an
argument a list of integers. It must find in that list all runs of 3
consecutive numbers that increase or decrease by 1. It should return the
list indices of the first element of each run. If there are no consecutive
runs it should return None.

Example: [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7] returns [0, 4, 6, 7]


Notes:

the "#:" comments on module level constants and the :param var:
style lines in the docstrings are picked up by the Sphinx
(www.sphinx-doc.org) documentation system.

"""

from __future__ import print_function # love it / hate it, Python 3 compat
import logging
import itertools


# setup logging
LOG_FORMAT = (
    '[%(asctime)s - %(filename)s - %(name)s - %(levelname)s] %(message)s')

# this will send logs to a file
logging.basicConfig(
    filename='alerun.log',
    filemode='a',              # change to 'w' to overwrite log file each run
    format=LOG_FORMAT,
    level=logging.DEBUG)

# this will send logs to the terminal
#logging.basicConfig(
#    format=LOG_FORMAT,
#    level=logging.DEBUG)


# from itertools cookbook
# tee can also be used here to setup
# a pair of iterators that are offset
# this recipe is not super clear, but it makes the code a bit more DRY
# and is a relatively commonly used recipe.
def _gen_window(seq, n):
    """Returns a sliding window (of width n) over data from the iterable
    s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
    """
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def _is_mono_skip(diffs, skip):
    """Test iterable of diffs to see if they are all equal to `skip` or -`skip`

    :param diffs: an iterable of intergers
    :type diffs: ``list`` or ``tuple``
    :param skip: amount by which consecutive numbers must increase or decrease
    :type skip: ``int``
    """
    # something has gone wrong if diffs is an empty list
    # also all([el==skip for el in diffs]) returns True for diffs=[]
    if len(diffs) < 1:
        raise Exception('length of diffs must be at least 1')
    mono_skip_pos = all([el==skip for el in diffs])  # O(window_size)
    mono_skip_neg = all([-el==skip for el in diffs]) # O(window_size)
    mono_skip = mono_skip_pos or mono_skip_neg
    return mono_skip


def find_consecutive_runs(search_me, skip=1, window_size=3):
    """Iterate over all runs of length `window_size` in `search_me` and test
    the runs for the property `mono_skip` (monotonically increasing/decreasing
    in increments of `skip`).  Return the starting index of each run that has
    the mono_skip property.

    :param search_me: input integers
    :type search_me: ``list``
    :param skip: amount by which consecutive numbers must increase or decrease
    :type skip: ``int``
    :param window_size: length of a run
    :type window_size: ``int``
    """
    # check window size
    if window_size < 2:
        raise Exception(
            'window size = {} but must be greater than 1'.format(window_size))

    n_elements = len(search_me)

    # check if one run fits
    if n_elements < window_size:
        logging.info(
            'input list length {} less than window size {}'
            .format(n_elements, window_size))
        return None

    # slide window and check each run
    run_indices = []
    for i_run, maybe_run in enumerate(_gen_window(search_me, window_size)):
        diffs = [pair[1] - pair[0] for pair in _gen_window(maybe_run, 2)]
        if _is_mono_skip(diffs, skip):
            run_indices.append(i_run)

    # return indices or None
    return run_indices if len(run_indices) > 0 else None



if __name__ == '__main__':
    search_me = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
    print('searching {}'.format(search_me))
    indices = find_consecutive_runs(search_me, skip=1, window_size=3)
    print('found run indices {}'.format(indices))
