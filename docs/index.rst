One Screenful of Python
=======================

A collection of short projects showcasing working Python code one screenful at
a time. The projects are intended to be useful in a classroom with minimum setup.
You can see the :ref:`background`, learn about :ref:`contributing`
or read on for an overview and the list of current projects.

This page is aimed at teachers looking to use the code and so assumes only
a basic amount of understanding of all the terminology. If you're a developer,
(possibly as well as being a teacher), see the section on :ref:`contributing`.

If you want to contribute ideas, corrections and so on, please use the issue
tracker or just email me: screenfuls@timgolden.me.uk.

Introduction
------------

The remit of the project is to produce useful Python code to be used in
classrooms. To reduce overhead for teachers, the following rules apply
to the code:

* The code should fit onto one screen (roughly) to keep it to a teachable size.

* The code should ideally run on Python 2.7 and 3.x to reduce problems from
  having the wrong version or selecting the wrong IDLE.

* The code should run cross-platform. Especially, it should run on Windows
  and on the Raspberry Pi as these are the most likely platforms to be
  found in the classroom.

* If the code is a longer project, it should be split up into separate
  steps, with each step introducing approximately a screenful of new code.
  This might also be done where several approaches are contrasted (as in the
  password-generator example).

Current Projects
----------------

Mr Bing
~~~~~~~

A simple PyGame example of the "bouncing ball" variety.

* **Code**: https://github.com/OneScreenfulOfPython/screenfuls/tree/master/MrBing
* **Zip**: https://github.com/OneScreenfulOfPython/screenfuls/archive/master.zip

Biggest File
~~~~~~~~~~~~

Find the biggest file in a directory

* **Code**: https://github.com/OneScreenfulOfPython/screenfuls/tree/master/BiggestFile
* **Zip**: https://github.com/OneScreenfulOfPython/screenfuls/archive/master.zip

Generate Password
~~~~~~~~~~~~~~~~~

Generate a password of a certain length: non-secure; essentially an exercise
in using the random module.

* **Code**: https://github.com/OneScreenfulOfPython/screenfuls/tree/master/GeneratePassword
* **Zip**: https://github.com/OneScreenfulOfPython/screenfuls/archive/master.zip

Room-Booking System
~~~~~~~~~~~~~~~~~~~

Users can book rooms via an RDBMS and a web form

* **Code**: https://github.com/OneScreenfulOfPython/booking-system
* **Zip**: https://github.com/OneScreenfulOfPython/booking-system/archive/master.zip


Ideas
-----

* Meta-idea: use the GitHub issue tracker for ideas
* Meta-idea: use readthedocs for documentation (or, at least, Sphinx)

* Race-condition: Demonstrate two processes running simultaneously, each trying to delete the same file. LBYL vs EAFP
* Countdown clock: Pygame-based countdown clock with alternative "faces"
* Password-cracker (brute force, use multiple machines).

Contents:

.. toctree::
   :maxdepth: 2

