#!/bin/bash

pandoc -s -o report.pdf README.md --listings -H headers.tex
