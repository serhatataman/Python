#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempts = 5

while pw != secret:
    count += 1
    if count > max_attempts: break
    pw = input(f"{count}: What's the secret word? ")
else:  # IMPORTANT: This else clause is executed if the while loop terminates normally. Meaning that the break is not encountered.
    auth = True

print("Authorized" if auth else "Calling the FBI...")

