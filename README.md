# Keylogger

This version of the program includes the following additional features:

    1. It uses the datetime module to get the current time in a more sophisticated way than the time module, and formats the time using the strftime method of a datetime object.
    
    2. It uses the getpass module to get the username of the current user.
    
    3. It uses the os module to get the hostname of the computer.
    
    4. It defines a save_record function that takes the elapsed time and key press count as arguments and writes them to the records.txt file along with the current date and time, username, and hostname.
    
    5. It catches both the KeyboardInterrupt and SystemExit exceptions, which allows the program to be interrupted using either CTRL+C or the exit command.

# Advance Keylogger

A Python script that records the number of key presses made by the user and the elapsed time between the start and end of the recording session. It saves this information to a file named `records.txt`.

The script uses the keyboard module to listen for key presses and keeps track of the number of key presses made by incrementing a counter. It also uses the time and datetime modules to calculate the elapsed time and record the current time when a record is saved.

When the user stops the recording session by pressing `Ctrl+C`, the script calculates the elapsed time and calls a `save_record` function to write the record to the `records.txt` file. The record contains the current time, the elapsed time, the number of key presses, the username of the user who ran the script, and the hostname of the computer the script is running on.

Overall, the script can be used to track how many key presses a user makes during a certain period of time, which can be useful for research, productivity analysis, or any other purposes that require measuring keyboard usage.
    
# Contribution

You can contribute to this project by analyzing the code and mention the tweaks by creating pull request.

# License

This project is under MIT License. So feel free to use it but also give the credits for the same.
