import sys, re, csv, time

files = sys.argv[1:]

data = []

csv_file_name = "merged.csv"
csvfile = open(csv_file_name, "w")


def mergefile(log_file_name):
    fh = open(log_file_name)

    fieldnames = ["remote_addr", "time", "url1", "url2", "agent"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        line = fh.readline()
        if not line:
            break

        line_data = re.search("([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).- -.\[(.*)\] \"[A-Z]+ (.*) .*\" [\d]+ [\d]+ \"(.*)\" \"(.*)\" .*", line)

        data = []
        ignore_count = 0
        
        if line_data !=  None:
            line_dict = {}
            line_dict["remote_addr"] = line_data.group(1)
            line_dict["time"] = line_data.group(2) #time.strptime(line_data.group(2),"%d/%b/%Y:%H:%S %z")
            line_dict["url1"] = line_data.group(3)
            line_dict["url2"] = line_data.group(4)
            line_dict["agent"] =  line_data.group(5)

            writer.writerow(line_dict)

        else:
            print "Ignored line: " + line

for filename in files:
    mergefile(filename)
