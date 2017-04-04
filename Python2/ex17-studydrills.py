# -*- coding: utf-8 -*-

# ex17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Make the core part one line long.
open(to_file, 'w').write(open(from_file).read())
#open(argv[2], 'w').write(open(argv[1]).read())
