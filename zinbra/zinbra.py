#!/usr/bin/env python
"""
Python wrapper for zinbra.xml
Usage: zinbra.py "${genome}" "${bed}" "${bin}" "${fdr}"
"""

import os
import sys
import subprocess

argv = sys.argv[1:]
print 'Arguments {0}'.format(argv)
genome, bed, bin, fdr = argv

# Configure main jar path
jar = os.environ.get("INTEGRATION_JAR")
print 'Using JAR distributive file {0}'.format(jar)

cmd = 'java -cp {0} org.jetbrains.bio.genestack.FastaToTwoBitCLA {1} reference.2bit'.format(jar, genome)
print 'Converting reference genome fasta to 2bit: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)

# See https://github.com/JetBrains-Research/zinbra for command line options
# cla.argument_string_list() is configured at ZinbraApplications#rebuildArgumentStringsFromVisualOptions
cmd = 'java -cp {0} org.jetbrains.bio.zinbra.ZinbraCLA ' \
      'analyze -i {1} -bed result.bed -r reference.2bit -b {3} -fdr {4}'.format(jar,
                                                                                bed,
                                                                                bin, fdr)
print 'Launching zinbra: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)
