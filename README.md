Screenfuls
==========

Examples of useful code using just one screenful of Python

Background
----------

At PyConUK 2013, we were told that a screenful of code was the right size
for a Secondary School teacher to fit nicely into one lesson plan. So
we were asked to produce whatever code we could -- ideally doing something
awesome -- in just one screenful of Python.

Instructions
------------

* Create a folder called MyExample or whatever

* Include a README which includes a useful description
  of what the example does / shows plus an indication of any
  platform-specific or version-specific stuff.

* Try to make the code platform- and version-agnostic, but feel
  free to showcase something specific if that makes sense. Some of
  the teachers will be limited as to target platform; others won't.

* Pure-stdlib solutions are definitely good (better, even).
  However, there's no point in producing complicated code just to 
  avoid importing. Just be clear where to get dependencies.
  If appropriate, include a pip requirements.txt

* Try to keep the root of your directory uncluttered: just the
  README and the code itself plus any necessary media.
  Use a subdirectory for screenshots or further explanations.
  Keep it simple.
  
* If we're just talking about one file, possibly with slightly different
  versions illustrating different tacks, use a folder within this screenfuls
  repo. If it needs more space (eg the Bookings System) create a separate
  repo.

Remember
--------

In a school context, there are often quite stringent
restrictions on what can be used / install etc. Teachers may
not be able to use the command line (eg to run sqlite.exe),
or may not be able to install arbitrary packages, at least not
without some bureaucratic overhead. Don't assume that "pip install X"
is always an acceptable approach.

These examples are intended to be used by teachers. Their
job is teaching, not delighting in the intracacies of Python
package dependencies, nor in understanding the argot of the
programmer's trade.

Keep it simple. If in doubt, err on the side of a Dummy's Guide.

Not Sure
--------

* Specify PEP8?
* Tests?
* Common modules?

Ideas
-----

* Meta-idea: use the GitHub issue tracker for ideas
* Meta-idea: use readthedocs for documentation (or, at least, Sphinx)

* Race-condition: Demonstrate two processes running simultaneously, each trying to delete the same file. LBYL vs EAFP
* Countdown clock: Pygame-based countdown clock with alternative "faces"
* Password Generator
