import pandas as pd
import os, sys
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(
        prog="BoroughComplaints",
        description="Find number of each complaint type per borough for given date range"
    )
    parser.add_argument("-i", "--input", help="input csv file")
    parser.add_argument("-s", "--start", help="start date (mm/dd/yyyy)")
    parser.add_argument("-e", "--end", help="end date (mm/dd/yyyy)")
    parser.add_argument("-o", "--output", help="output file",
                        default=sys.stdout)
    
    args = parser.parse_args()
    start_date = pd.to_datetime(args.start)
    end_date = pd.to_datetime(args.end)

    data = pd.read_csv(args.input)
    data['created_date'] = pd.to_datetime(data['created_date'])
    data = data[(data["created_date"] > start_date) & (data["created_date"] < end_date)]

    summary = data.groupby(['complaint_type', 'borough']).size()
    summary.to_csv(args.output)

    
if __name__ == "__main__":
    main()