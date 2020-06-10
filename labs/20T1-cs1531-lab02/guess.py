def guess(lo, hi):
    prev = round((hi+lo)/2)
    print(f"My guess is {prev}")
    ans = input("Is my guess too low (L), too high (H), or correct (C)?\n")
    if ans == 'C':
        print("Got it!")
        return
    elif ans == 'L':
        guess(prev, hi)
    elif ans == 'H':
        guess(lo, prev)
    else:
        print("Invalid response")

print("Pick a number between 1 and 100 (inclusive)")
ready = False
while not ready:
    response = input("Type in 'ok' once you are ready\n")
    if response == "ok":
        ready = True
guess(0, 100)
