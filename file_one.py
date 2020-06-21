#!/usr/bin/env python
import csv
with open("electronic_transactions.csv") as file:
    read_file=csv.reader(file)
    all_data=list(read_file)
    for i in all_data[:1]:
        headers=""
        for j in i:
            headers=headers+j+ " | "

        print("\n\n"+headers)
        print("_"*(len(headers)))
    for i in all_data[1:]:
        values=""
        for j in i:
            values=values+j+ " | "
        print(values)
