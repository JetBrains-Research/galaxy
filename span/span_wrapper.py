#!/usr/bin/env python

import os
import shutil
import subprocess
import sys

argv = sys.argv[1:]
print 'Arguments {0}'.format(argv)

SPAN_JAR = os.environ.get("SPAN_JAR")
print 'Using SPAN Peak Analyzer distributive file {0}'.format(SPAN_JAR)

MEMORY = argv[0]
THREADS = argv[1]
ACTION = argv[2]
argv = argv[3:]

working_dir = os.path.abspath('.')
print 'WORKING DIRECTORY: {}'.format(working_dir)


def link(name, f):
    """ SPAN uses file extension to detect input type, so original names are necessary, instead of Galaxy .dat files"""
    result = os.path.join(working_dir, name)
    if not os.path.exists(result):
        os.symlink(f, result)
    return result


if ACTION == 'model_with_control':
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     control, control_file,
     bin) = argv
    cmd = 'java -Xmx{}m -jar {} analyze --threads {} ' \
          '--chrom.sizes {} --treatment {} --control {} --bin {}'.format(
        MEMORY, SPAN_JAR, THREADS,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        link(control, control_file),
        bin)

elif ACTION == 'model_without_control':
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     bin) = argv
    cmd = 'java -Xmx{}m -jar {} analyze --threads {} ' \
          '--chrom.sizes {} --treatment {} --bin {}'.format(
        MEMORY, SPAN_JAR, THREADS,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        bin)

elif ACTION == "peaks_with_control":
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     control, control_file,
     bin,
     fdr, gap) = argv
    cmd = 'java -Xmx{}m -jar {} analyze --threads {} ' \
          '--chrom.sizes {} --treatment {} --control {} --bin {} --fdr {} --gap {} --peaks {}'.format(
        MEMORY, SPAN_JAR, THREADS,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        link(control, control_file),
        bin, fdr, gap,
        os.path.join(working_dir, 'result.peak'))

elif ACTION == 'peaks_without_control':
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     bin,
     fdr, gap) = argv
    cmd = 'java -Xmx{}m -jar {} analyze --threads {} ' \
          '--chrom.sizes {} --treatment {} -bin {} --fdr {} --gap {} --peaks {}'.format(
        MEMORY, SPAN_JAR, THREADS,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        bin, fdr, gap,
        os.path.join(working_dir, 'result.peak'))
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     bin,
     fdr, gap) = argv

else:
    raise Exception("Unknown action command {}".format(ACTION))

print 'Launching SPAN: {}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)

# Move model to the the working dir with given name
fit_dir = os.path.join(working_dir, 'fit')
model_original = os.path.join(fit_dir, os.listdir(fit_dir)[0])
shutil.move(model_original, os.path.join(working_dir, 'model.span'))

# Move log file
logs_dir = os.path.join(working_dir, 'logs')
log_original = os.path.join(logs_dir, os.listdir(logs_dir)[0])
shutil.move(log_original, os.path.join(working_dir, "span.log"))
