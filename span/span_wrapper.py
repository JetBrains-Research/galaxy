#!/usr/bin/env python

import os
import sys
import subprocess
argv = sys.argv[1:]
print 'Arguments {0}'.format(argv)

SPAN_JAR = os.environ.get("SPAN_JAR")
# span.jar from Docker container
# SPAN_JAR = "/root/span.jar"
print 'Using SPAN Peak Analyzer distributive file {0}'.format(SPAN_JAR)

# #if $action.action_selector
#     #if str($control.control_selector) == "with_control"
#         span_wrapper.py model with_control "${genome}" "${treatment_file}" "${bin}" "${action.model_file}" "${control.control_file}"
#     #else
#         span_wrapper.py model without_control "${genome}" "${treatment_file}" "${bin}" "${action.model_file}"
#     #end if
# #else
#     #if $control.control_selector
#         span_wrapper.py peaks with_control "${genome}" "${treatment_file}" "${bin}" "${action.model_file}" "${control.control_file}" "${fdr}" "${gap}" "${action.peaks_file}"
#     #else
#         span_wrapper.py peaks without_control "${genome}" "${treatment_file}" "${bin}" "${action.model_file}" "${fdr}" "${gap}" "${action.peaks_file}"
#     #end if
# #end if

# See http://artyomovlab.wustl.edu/aging/span.html for command line options
action = argv[0]
control = argv[1]
if action == 'model':
    if control == 'with_control':
        (chrom_sizes, treatment_file, bin, model_file, control_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --control {} --bin {}'.format(
            SPAN_JAR, chrom_sizes, treatment_file, control_file, bin
        )
        print "MODEL FILE" + model_file
    elif control == 'without_control':
        (chrom_sizes, treatment_file, bin, model_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --bin {}'.format(
            SPAN_JAR, argv[2], argv[3], argv[4]
        )
        print "MODEL FILE" + model_file
    else:
        raise Exception("Unknown control option {}".format(control))

elif action == "peaks":
    if control == 'with_control':
        (chrom_sizes, treatment_file, bin, model_file, control_file, fdr, gap, peaks_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --control {} --bin {} --fdr {} --gap {} --peaks {}'.format(
            SPAN_JAR, chrom_sizes, treatment_file, control_file, bin, fdr, gap, peaks_file
        )
        print "MODEL FILE" + model_file
    elif control == 'without_control':
        (chrom_sizes, treatment_file, bin, model_file, fdr, gap, peaks_file) = argv[2:]
        cmd = 'java -jar {} analyze --chrom.sizes {} --treatment {} --bin {} --fdr {} --gap {} --peaks {}'.format(
            SPAN_JAR, chrom_sizes, treatment_file, bin, fdr, gap, peaks_file
        )
        print "MODEL FILE" + model_file
    else:
        raise Exception("Unknown control option {}".format(control))
else:
    raise Exception("Unknown action command {}".format(action))


print 'Launching SPAN: {0}'.format(cmd)
subprocess.check_call(cmd, cwd=None, shell=True)
