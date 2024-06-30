#  Exception handling program
#try
#except
#finally

cb=10000
while True:
    wb=int(input("Enter amount"))

    try:
        if(cb<wb):
            raise ValueError()
        cb=cb-wb
        print("Mony Sent")
        print("Current Bal is:",cb)
    except:
        print("Insufficient Balance.")
        print("Current balance is",cb)
    finally:
        print("Bye")