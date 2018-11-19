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
#     #if str($control_file) != 'None':
#         span_wrapper.py model_with_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${control_identifier}" "${control.control_file}"
#             "${bin}"
#
#     #else
#         span_wrapper.py model without_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${bin}"
#     #end if
# #else
#     #if str($control_file) != 'None':
#         span_wrapper.py peaks_with_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${control_identifier}" "${control.control_file}"
#             "${bin}"
#             "${action.fdr}" "${action.gap}"
#     #else
#         span_wrapper.py peaks_without_control
#             "${genome_identifier}" "${genome_file}"
#             "${treatment_identifier}" "${treatment_file}"
#             "${bin}"
#             "${action.fdr}" "${action.gap}"
#     #end if
# #end if
action = argv[0]

working_dir = os.path.abspath('.')
print 'WORKING DIRECTORY: {}'.format(working_dir)


def link(name, f):
    """ SPAN uses file extension to detect input type, so original names are necessary, instead of Galaxy .dat files"""
    result = os.path.join(working_dir, name)
    if not os.path.exists(result):
        os.symlink(f, result)
    return result


if action == 'model_with_control':
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     control, control_file,
     bin) = argv[1:]
    cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --control {} --bin {}'.format(
        SPAN_JAR,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        link(control, control_file),
        bin)
elif action == 'model_without_control':
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     bin) = argv[1:]
    cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --bin {}'.format(
        SPAN_JAR,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        bin)
elif action == "peaks_with_control":
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     control, control_file,
     bin,
     fdr, gap) = argv[1:]
    cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --control {} ' \
          '--bin {} --fdr {} --gap {} --peaks {}'.format(
        SPAN_JAR,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        link(control, control_file),
        bin, fdr, gap,
        os.path.join(working_dir, 'result.peak'))
elif action == 'peaks_without_control':
    (chrom_sizes, chrom_sizes_file,
     treatment, treatment_file,
     bin,
     fdr, gap) = argv[1:]
    cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} -' \
          '-bin {} --fdr {} --gap {} --peaks {}'.format(
        SPAN_JAR,
        link(chrom_sizes, chrom_sizes_file),
        link(treatment, treatment_file),
        bin, fdr, gap,
        os.path.join(working_dir, 'result.peak'))
else:
    raise Exception("Unknown action command {}".format(action))

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
