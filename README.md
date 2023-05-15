# Keylogger

This version of the program includes the following additional features:

   
    
    5. It catches both the KeyboardInterrupt and SystemExit exceptions, which allows the program to be interrupted using either CTRL+C or the exit command.

# Advance Keylogger

   1. A Python script that records the number of key presses made by the user and the elapsed time between the start and end of the recording session. It saves this information to a file named `records.txt`.

   2. The script uses the keyboard module to listen for key presses and keeps track of the number of key presses made by incrementing a counter. It also uses the time and datetime modules to calculate the elapsed time and record the current time when a record is saved.

   3. When the user stops the recording session by pressing `Ctrl+C`, the script calculates the elapsed time and calls a `save_record` function to write the record to the `records.txt` file. The record contains the current time, the elapsed time, the number of key presses, the username of the user who ran the script, and the hostname of the computer the script is running on.

   4. Overall, the script can be used to track how many key presses a user makes during a certain period of time, which can be useful for research, productivity analysis, or any other purposes that require measuring keyboard usage

# File Format

The records.txt file contains one record per line. Each record contains the following fields:

    => Current time
    => Elapsed time (in seconds)
    => Key press count
    => User
    => Host

The fields are separated by commas. Here's an example record:
``` java
2023-04-09 10:15:23, Elapsed time = 37.52 seconds, Key press count = 122, User = ryx, Host = mycomputer
```
    
# Contribution

You can contribute to this project by analyzing the code and mention the tweaks by creating pull request.

# License

This project is under MIT License. So feel free to use it but also give the credits for the same.
