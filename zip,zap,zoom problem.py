def display(num):
    if num%3==0 and num%5==0:
        print("Zoom")
    elif num%3==0:
        print("Zip")
    elif num%5==0:
        print("Zap")
    else:
        print("Invallid")
    return display

message=display(15)