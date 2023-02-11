secret_word = "jimcaale"
gest = ""
gest_count = 0
gest_Limit = 3
out_ofgest = False
while gest != secret_word and not(out_ofgest):
    if gest_count < gest_Limit:
        gest = input("enter the gest word")
        gest_count += 1
    else:
        out_ofgest = True
if out_ofgest:
    print ("you loze ")
else:
    print("you win")