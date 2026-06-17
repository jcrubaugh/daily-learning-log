
line_count = 0
with open ("raw_logs.txt","r") as logs:
    for line in logs:
        if "status:failed" in line:
            line_count += 1
print(f"Successfully extracted {line_count} rows of log data")
