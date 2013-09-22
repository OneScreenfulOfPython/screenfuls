Find the biggest file in a directory structure.

Uses a recursive generator to walk down the directory structure,
iterating over filenames. Feeds that into the builtin max function
with a os.path.getsize function to find the top by size.