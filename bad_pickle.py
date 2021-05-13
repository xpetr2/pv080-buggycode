"""
contains bunch of buggy examples
taken from
https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
"""
from subprocess import call, Popen
import base64
try:
    import cPickle as pickle
except _:
    import pickle


# Input injection
def transcode_file(filename):
    """Input injection"""
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    call(command, shell=True)  # a bad idea!


# Assert statements
def foo_assert(user):
    """Assert statements"""
    assert user.is_admin, 'user does not have access'
   # secure code...


# Pickles
class RunBinSh():
    """Pickles"""
    def __reduce__(self):
        return (Popen, (('/bin/sh',),))


print(base64.b64encode(pickle.dumps(RunBinSh())))
