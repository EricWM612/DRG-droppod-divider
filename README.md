# DRG Droppod Divider
Simple Python script to divide groups of arbitrary size into even-ish groups for the game Deep Rock Galactic (or similar)

In order to divide a group up, simply run the script in a terminal and tell it how many players you want to make groups out of. By default, each player will be assigned a number, and each number will be assigned a pod.
Great for party groups who have too many members for a single group, and would prefer to mix up groups for each round.

In order to provide names instead of numbers, edit the script to make the constant `NAMED` to `True`. Provided names will then be assigned pods in the same way, but it makes it easier for you to determine who is in what pod.

The script is fairly simple and doesn't take into account class, preferences, etc. Instead, it just seeks to create "party groups" evenly and randomly.
