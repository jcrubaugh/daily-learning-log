
line_count = 0
with open ("raw_logs.txt","r") as infile, open ("failed_Comms.txt", "w") as outfile:
    for line in infile:
        if "status:failed" in line:
            outfile.write(line)
print(f"Pipeline complete. Failed Logs exported")
