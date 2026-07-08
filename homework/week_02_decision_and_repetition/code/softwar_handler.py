while True:
    user_input = input("Enter command for s/w (start/stop/pause): ")

    match user_input:
        case "start":
            print("s/w Starting...")
        case "stop":
            print("s/w Stopping...")
        case "pause":
            print("s/w Pausing...")
        case _:
            print("Unknown command, please enter valid comand again")

    sw_stop = input("Do you want to stop the program? (yes/no): ")
    if sw_stop == "yes":
        
        break        