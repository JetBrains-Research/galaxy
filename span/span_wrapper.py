#!/usr/bin/env python

import os
import shutil
import subprocess
import sys

argv = sys.argv[1:]
print 'Arguments {0}'.format(argv)

SPAN_JAR = os.environ.get("SPAN_JAR")
print 'Using SPAN Peak Analyzer distributive file {0}'.format(SPAN_JAR)

# #if str($action.action_selector) == "model"
#     #if $control.control_selector
#         span_wrapper.py model with_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${bin}" "${action.model_file}"
#             "${control_identifier}" "${control.control_file}"
#     #else
#         span_wrapper.py model without_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${bin}" "${action.model_file}"
#     #end if
# #else
#     #if $control.control_selector
#         span_wrapper.py peaks with_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${bin}" "${action.model_file}"
#             "${control_identifier}" "${control.control_file}"
#             "${fdr}" "${gap}" "${action.peaks_file}"
#     #else
#         span_wrapper.py peaks with_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${bin}" "${action.model_file}"
#             "${fdr}" "${gap}" "${action.peaks_file}"
#     #end if
# #end if

# See https://research.jetbrains.org/groups/biolabs/tools/span-peak-analyzer for command line options
action = argv[0]
control = argv[1]

working_dir = os.path.abspath('.')
print 'WORKING DIRECTORY: {}'.format(working_dir)


def link(name, f):
    """ SPAN uses file extension to detect input type, so original names are necessary, instead of Galaxy .dat files"""
    result = os.path.join(working_dir, name)
    os.symlink(f, result)
    return result


if action == 'model':
    if control == 'with_control':
        (chrom_sizes, chrom_sizes_file,
         treatment, treatment_file,
         bin, model_file,
         control, control_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --control {} --bin {}'.format(
            SPAN_JAR,
            link(chrom_sizes, chrom_sizes_file),
            link(treatment, treatment_file),
            link(control, control_file),
            bin
        )
    elif control == 'without_control':
        (chrom_sizes, chrom_sizes_file,
         treatment, treatment_file,
         bin, model_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --bin {}'.format(
            SPAN_JAR,
            link(chrom_sizes, chrom_sizes_file),
            link(treatment, treatment_file),
            bin
        )
    else:
        raise Exception("Unknown control option {}".format(control))

elif action == "peaks":
    if control == 'with_control':
        (chrom_sizes, chrom_sizes_file,
         treatment, treatment_file,
         bin, model_file,
         control, control_file,
         fdr, gap, peaks_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --control {} --bin {} --fdr {} --gap {} --peaks {}'.format(
            SPAN_JAR,
            link(chrom_sizes, chrom_sizes_file),
            link(treatment, treatment_file),
            link(control, control_file),
            bin, fdr, gap,
            os.path.join(working_dir, peaks_file)
        )
    elif control == 'without_control':
        (chrom_sizes, chrom_sizes_file,
         treatment, treatment_file,
         bin, model_file,
         fdr, gap, peaks_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --bin {} --fdr {} --gap {} --peaks {}'.format(
            SPAN_JAR,
            link(chrom_sizes, chrom_sizes_file),
            link(treatment, treatment_file),
            bin, fdr, gap,
            os.path.join(working_dir, peaks_file)
        )
    else:
        raise Exception("Unknown control option {}".format(control))
else:
    raise Exception("Unknown action command {}".format(action))


print 'Launching SPAN: {}'.format(cmd)
print 'Model file: {}'.format(model_file)
try:
    print 'Peaks file: {}'.format(peaks_file)
except NameError:
    pass

subprocess.check_call(cmd, cwd=None, shell=True)

# Move model to the the working dir with given name
fit_dir = os.path.join(working_dir, 'fit')
model_original = os.path.join(fit_dir, os.listdir(fit_dir)[0])
shutil.move(model_original, os.path.join(working_dir, model_file))

# Move log file
logs_dir = os.path.join(working_dir, 'logs')
log_original = os.path.join(logs_dir, os.listdir(logs_dir)[0])
shutil.move(log_original, os.path.join(working_dir, "span.log"))
