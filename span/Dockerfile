FROM openjdk:8-jre-alpine

USER root

# Prepare span_wrapper.py
COPY span_wrapper.py /usr/local/bin/
RUN chmod a+x /usr/local/bin/span_wrapper.py

# Download SPAN Peak Analyzer, see details: http://artyomovlab.wustl.edu/aging/span.html
RUN wget https://download.jetbrains.com/biolabs/span/span-0.7.1.4272.jar -O /root/span.jar