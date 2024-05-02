#A-adult passenger,C-child,FC-flight caption,FA-flight attendent,SP-suspicious passenger
for passenger in "A","A","FC","C","FA","SP","A","A":
    if(passenger=="FC" or passenger=="FA"):
        print("no check required")
        continue
    if (passenger=="SP"):
        print("declare emergency in the airport ")
        break
    if (passenger=="A" or passenger=="C"):
        print("proceed  with normal security check")

print("check the person")
print("check for cabin baggage")
