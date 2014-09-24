Generate Password
=================

The challenge: to generate a useful password of a certain length,
possibly accounting for certain restrictions (letters, numbers etc.)

Additional work could include algorithms to help make it memorable

NB Obvious disclaimer: nothing done here will produce cryptographically
secure passwords. It's more about exercising the ideas involved in
random selection -- and passwords is an obvious application of that.

Version 1
---------

This is the simplest version: all characters are candidates for inclusion
in the generated password: letters, numbers & punctuation. Other than length,
there are no other restrictions.

Version 2
---------

This is more sophisticated, allowing the user to specify that there be
at least one of each of the sets of characters.

Version 3
---------

This does something different, putting together words from a corpus
of texts to form passwords which are more memorable.