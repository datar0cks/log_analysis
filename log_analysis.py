#!/usr/bin/python

from newsdb import run_report
from reportconfig import *


if __name__ == '__main__':
    print("\r\n*****************************")
    print("******** Run Reports ********")
    print("*****************************\r\n")

    for key in sorted(report_list.keys()):
        print("%s --> %s" % (key, report_list[key][1]))

    report_selection = raw_input("\r\nSelect report to run:  ")
    report_type = report_list.get(report_selection, [None, None, None])[0]
    result_type = report_list.get(report_selection, [None, None, None])[2]

    if report_type:
        result = run_report(report_type)
        for row in result:
            print(" -- ".join(str(element) for element in row) +
                  " %s" % (result_type))
