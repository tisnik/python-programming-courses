#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Simple preprocessor for Markdown files that handles @ character as include statement."""

input_file = "Python2.md"
output_file = "Python2_.md"

with open(input_file, "r") as fin:
    with open(output_file, "w") as fout:
        for line in fin.readlines():
            # handle @ character at the beginning of line as include statement
            if line[0] == "!":
                # retrieve file name of file to be included
                include = line[2:].strip()
                print("including:", include)

                # perform the inclusion within ```python block
                fout.write("```python\n")
                with open(include, "r") as inc:
                    included = inc.read()
                fout.write(included)
                fout.write("```\n")
            # other lines are to be output in its original form
            else:
                fout.write(line)
