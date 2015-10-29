#!/usr/bin/env python

import os
import sys
import subprocess

argv = sys.argv[1:]
print 'Arguments {0}'.format(argv)

# Check command
if len(argv) == 4:
    genome, fdr, action, bam = argv
    assert action == "analyze"
else:
    genome, fdr, action, bam1, bam2 = argv
    assert action == "compare"

# Configure main jar path
jar = os.environ.get("INTEGRATION_JAR")
print 'Using JAR distributive file {0}'.format(jar)

cmd = 'java -cp {0} org.jetbrains.bio.genestack.FastaToTwoBitCLA {1} reference.2bit'.format(jar, genome)
print 'Converting reference genome fasta to 2bit: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)

# See https://github.com/JetBrains-Research/cmeth for command line options
if action == "analyze":
    cmd = 'java -cp {0} org.jetbrains.bio.cmeth.CmethCLA ' \
          'analyze -i {1} -r reference.2bit -fdr {2}'.format(jar, bam, fdr)
else:
    cmd = 'java -cp {0} org.jetbrains.bio.cmeth.CmethCLA ' \
          'compare -1 {1} -2 {2} -r reference.2bit -fdr {3}'.format(jar, bam1, bam2, fdr)
print 'Launching cmeth: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)
