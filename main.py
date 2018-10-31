import UI

# create an instance of the UI
ui = UI.UI()

# set application to running
running = True
while running:
    s = input("Enter a command: ")

    # stop and quit application
    if s == "q":
        running = False
    else:
        # take input and attempt to change into a command
        ui.command(s)

print("Program has been terminated.")

