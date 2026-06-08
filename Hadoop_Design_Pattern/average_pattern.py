# MAPPER CODE 
#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

next(reader)

for row in reader:
    region = row[1]
    days = int(row[2])

    print(f"{region}\t{days}")


# REDUCER CODE
