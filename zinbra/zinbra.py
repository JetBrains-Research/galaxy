#!/usr/bin/env python
"""
Python wrapper for zinbra.xml
"""

import os
import sys
import subprocess

argv = sys.argv[1:]
print 'Arguments {0}'.format(argv)

# Check command
if len(argv) == 5:
    genome, bin, fdr, action, bed = argv
    assert action == "analyze"
else:
    genome, bin, fdr, action, bed1, bed2 = argv
    assert action == "compare"

# Configure main jar path
jar = os.environ.get("INTEGRATION_JAR")
print 'Using JAR distributive file {0}'.format(jar)

cmd = 'java -cp {0} org.jetbrains.bio.genestack.FastaToTwoBitCLA {1} reference.2bit'.format(jar, genome)
print 'Converting reference genome fasta to 2bit: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)

# See https://github.com/JetBrains-Research/zinbra for command line options
if action == "analyze":
    cmd = 'java -cp {0} org.jetbrains.bio.zinbra.ZinbraCLA ' \
          'analyze -i {1} -bed result.bed -r reference.2bit -b {3} -fdr {4}'.format(jar, bed, bin, fdr)
else:
    cmd = 'java -cp {0} org.jetbrains.bio.zinbra.ZinbraCLA ' \
          'compare -1 {1} -2 {2} -bed result.bed -r reference.2bit -b {3} -fdr {4}'.format(jar, bed1, bed2, bin, fdr)
print 'Launching zinbra: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)
