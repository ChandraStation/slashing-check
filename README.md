# Slash Amount Checker 
A simple py script that takes two json files and outputs the amount of tokens that have been slashed organized from greatest to least based off delegator addresses. 

### How to use
You will need two json files. One file before the slash, the other file after the slash. Listed below are the commands you can use to get said files.

* Pre Slash ```{daemon} q staking delegations-to {valoper-address} --height {height right before the slash} --node {rpc node} --chain-id {chain-id} --limit {amount of delegations} --output json > pre-slash.json```

* Post Slash ```{daemon} q staking delegations-to {valoper-address} --height {height right after the slash} --node {rpc node} --chain-id {chain-id} --limit {amount of delegations} --output json > post-slash.json```

Keep in mind nodes are usually pruning their data which means they most likely will not contain the blocks you are querying for, unless it is right after the slashing event. **Please use an archive node**

### Run
1. Install Python

2. `python3 my_script.py pre-slash.json post-slash.json output.json --decimal-places 6`

the script accepts either 18 or 6 decimal places as a flag. The output will contain the data. 