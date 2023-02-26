import json
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Compute delegation changes')
parser.add_argument('pre_file', help='the pre-slash JSON file')
parser.add_argument('post_file', help='the post-slash JSON file')
parser.add_argument('out_file', help='the output JSON file')
parser.add_argument('--decimal-places', type=int, default=18, choices=[6, 18], help='the number of decimal places to round to (default: 18)')
args = parser.parse_args()

# Load the initial JSON file and store the amounts indexed by the delegator address
with open(args.pre_file, 'r') as f:
    initial_data = json.load(f)

initial_amounts = {}
for response in initial_data['delegation_responses']:
    delegator_address = response['delegation']['delegator_address']
    initial_amount = int(response['balance']['amount'])
    initial_amounts[delegator_address] = initial_amount

# Load the updated JSON file and subtract the amounts
with open(args.post_file, 'r') as f:
    updated_data = json.load(f)

changes = {}
for response in updated_data['delegation_responses']:
    delegator_address = response['delegation']['delegator_address']
    if delegator_address in initial_amounts:
        updated_amount = int(response['balance']['amount'])
        initial_amount = initial_amounts[delegator_address]
        change = round((initial_amount - updated_amount) / 10**args.decimal_places, args.decimal_places)
        changes[delegator_address] = change

# Sort the changes dictionary by value (change) in descending order
sorted_changes = {k: v for k, v in sorted(changes.items(), key=lambda item: item[1], reverse=True)}

# Compute the total of all changes
total = sum(sorted_changes.values())

# Write the sorted changes dictionary and the total to a new JSON file
with open(args.out_file, 'w') as f:
    json.dump({'changes': sorted_changes, 'total': total}, f, indent=4)
