import json
from datetime import datetime
import math
import pandas as pd

# Load local JSON file
with open('C:/Users/DELL/Complexity_parser/Scripts/closed_issues_robotframework.json', 'r') as json_file:
    data = json.load(json_file)

# Extract label names and count occurrences of "bug"
bug_count = sum(1 for issue in data if 'bug' in [label['name'] for label in issue['labels']])

print(f'Number of bugs: {bug_count}')

tbf_data = []
issue_ids = []  # New list to store issue IDs
for issue in data:
    created_at = datetime.fromisoformat(issue['created_at'].replace("Z", "+00:00"))
    closed_at = datetime.fromisoformat(issue['closed_at'].replace("Z", "+00:00"))
    tbf = closed_at - created_at
    tbf_data.append(tbf.days)  # Convert TBF to days and store in the list
    issue_ids.append(issue['id'])  # Store issue IDs

# Step 1: Calculate Mean Time Between Failures (MTBF)
mtbf = sum(tbf_data) / len(tbf_data)

# Step 2: Calculate Reliability for Each Issue
reliabilities = [math.exp(-tbf / mtbf) for tbf in tbf_data]

# Step 3: Calculate System Reliability (Product of Individual Reliabilities)
system_reliability = 1
for reliability in reliabilities:
    system_reliability *= reliability

# Print the results
print(f"Mean Time Between Failures (MTBF): {mtbf} days")
#print(f"Reliabilities for Each Issue: {reliabilities}")
#print(f"System Reliability: {system_reliability}")

# Create a DataFrame for results

data = {'Number': [issue['number'] for issue in data], 'Issue ID': issue_ids, 'TBF': tbf_data, 'Reliability': reliabilities}
df = pd.DataFrame(data)


# Save to a CSV file
df.to_csv('Consequences.csv', index=False)
