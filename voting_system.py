candidates = {
    "A": 0,
    "B": 0,
    "C": 0
}

voters = int(raw_input("Enter number of voters: "))

for i in range(voters):
    print("\nCandidates: A, B, C")
    vote = raw_input("Enter your vote: ").upper()

    if vote in candidates:
        candidates[vote] += 1
        print("Vote recorded.")
    else:
        print("Invalid vote.")

print("\n--- Voting Results ---")

for candidate in candidates:
    print(candidate, ":", candidates[candidate], "votes")

winner = max(candidates, key=candidates.get)

print("Winner:", winner)
