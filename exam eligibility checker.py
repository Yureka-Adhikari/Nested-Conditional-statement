m_cause=input("Did you have any medical cause? Y or N?: ")
attendance=int(input("Enter the attendance of the student: "))

if m_cause == "Y" or m_cause== "y":
    print("You are allowed")
else:
    if attendance >= 75:
        print("allowed")
    else:
        print("NOTTTT allowed")