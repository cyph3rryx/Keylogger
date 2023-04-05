# Keylogger

This version of the program includes the following additional features:

    1. It uses the datetime module to get the current time in a more sophisticated way than the time module, and formats the time using the strftime method of a datetime object.
    
    2. It uses the getpass module to get the username of the current user.
    
    3. It uses the os module to get the hostname of the computer.
    
    4. It defines a save_record function that takes the elapsed time and key press count as arguments and writes them to the records.txt file along with the current date and time, username, and hostname.
    
    5. It catches both the KeyboardInterrupt and SystemExit exceptions, which allows the program to be interrupted using either CTRL+C or the exit command.
    
# Contribution

You can contribute to this project by analyzing the code and mention the tweaks by creating pull request.
