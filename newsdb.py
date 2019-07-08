#!/usr/bin/python

import psycopg2
from reportconfig import *


def run_report(report_type):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(report_query.get(report_type))
    results = c.fetchall()
    db.close()

    return results
