# Copyright (c) 2021, Neil Booth
#
# All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


__all__ = (
    'JSONFlags',
)


from enum import IntFlag


class JSONFlags(IntFlag):
    '''Flags controlling conversion of transactions and scripts to JSON.'''
    # Include the index of each input
    ENUMERATE_INPUTS = 1 << 0
    # Include the index of each output
    ENUMERATE_OUTPUTS = 1 << 1
    # Include the transaction size in bytes
    SIZE = 1 << 2
    # Include a human-readable description of the locktime constraint is output
    LOCKTIME_MEANING = 1 << 3
    # Include classification of output scripts
    CLASSIFY_OUTPUT_SCRIPT = 1 << 4
    # Display signature sighashes as text
    SIGHASH_MEANING = 1 << 5
