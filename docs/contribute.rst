.. _contribute:

How to Contribute
=================

Pre-requisites
--------------

This guide assumes that you're familiar with the workings of git and
Github, at least enough to know how to fork, clone, commit, push and issue
a pull request. If you're not, but you still want to contribute in the
shape of ideas, projects or corrections, please use the issue tracker
and post text or code:

FIXME: http://github.com/.../

We welcome any suggestion although some ideas may not fit so well with
the project's remit.

Rules
-----

* The code should fit onto one screen (roughly). The point is to keep
  the code to a teachable size.

* The code should ideally run on Python 2.7 and 3.x. This can be achieved
  with conditional imports or six, but it might be better to stick to
  one version if compatibility hurts readability.

* The code should run cross-platform. Especially, it should run on Windows
  and on the Raspberry Pi as these are the most likely platforms to be
  found in the classroom.

* If the code is a longer project, it should be split up into separate
  steps, with each step introducing approximately a screenful of new code.
  This might also be done where several approaches are contrasted (as in the
  password-generator example).


Instructions
------------

* Create a folder called MyExample or whatever to hold your code.

* Include a README, ideally in ReST format but at least in legible text,
  which includes a useful description of what the example does / shows
  plus an indication of platform-specific or version-specific aspects.

* Try to make the code platform- and version-agnostic, but feel
  free to showcase something specific if that makes sense. Some of
  the teachers will be limited as to target platform; others won't.

* Code should be PEP8-compliant.

* Pure-stdlib solutions are definitely good because they reduce the complexity
  of getting the code up-and-running. Also they showcase how much functionality
  comes for free within Python itself.

  However, there's no point in producing complicated code just to
  avoid importing. Just be clear where to get dependencies.
  If appropriate, include a pip requirements.txt. Some schools may
  have restrictions which prevent them from installing arbitrary packages.

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
