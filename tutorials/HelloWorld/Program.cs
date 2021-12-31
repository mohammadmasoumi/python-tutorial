using System;
using System.Collections.Generic;

class School {
    // commands
    const string INPUT_USER = "InputUser"; 
    const string INPUT_BOOK = "InputBook";
    const string USER_SHOW = "UserShow";
    const string BOOK_SHOW = "BookShow";
    const string BOOK_SUBJECT = "BookSubject";
    const string EDIT_USER = "EditUser";
    const string EXIT = "Exit";
        
    static void Main(string[] args) {   
        // declare variables
        int userCounter = 0;
        int bookCounter = 0;
        string inputString, command;

        // get books # 
        Console.WriteLine("Enter total books:");
        int totalBooks = int.Parse(Console.ReadLine() ?? "0");
        
        // get users # 
        Console.WriteLine("Enter total user:");
        int totalUsers = int.Parse(Console.ReadLine() ?? "0");

        // store user's and book's info
        string[,] booksArray = new string[totalBooks, 2];
        string[,] usersArray = new string[totalUsers, 2];

        // List<string> users = new List<string>();

        while (true) {
            inputString = Console.ReadLine() ?? "";

            string[] splittedInput =  inputString.Split(" ");
            command = splittedInput[0];

            if (command == EXIT){
                break;

            } else if (command == INPUT_USER){
                if (splittedInput.Length == 3){
                    usersArray[userCounter, 0] = splittedInput[1];
                    usersArray[userCounter, 1] = splittedInput[2];
                    userCounter++;
                } else {
                    Console.WriteLine("[Invalid command]: InputUser needs 3 arguments.");
                }

            } else if (command == INPUT_BOOK) { 
                if (splittedInput.Length == 3 && bookCounter < totalBooks){
                    booksArray[bookCounter, 0] = splittedInput[1];
                    booksArray[bookCounter, 1] = splittedInput[2];
                    bookCounter++;
                } else {
                    Console.WriteLine("[Invalid command]: InputBook needs 3 arguments.");
                }

            } else if (command == USER_SHOW) {
                Console.WriteLine("------------------ Users ------------------");

                for (int index = 0; index < usersArray.GetUpperBound(0); index++) {
                    Console.WriteLine("[" + index.ToString() + "]: firstName: " + usersArray[index, 0] + " ,LastName: " + usersArray[index, 1]);
                }

            } else if (command == BOOK_SHOW) {
                Console.WriteLine("------------------ Books ------------------");

                for (int index = 0; index < booksArray.GetUpperBound(0); index++) {
                    Console.WriteLine("[" + index.ToString() + "]: bookName: " + booksArray[index, 0] + " Subject: " + booksArray[index, 1]);
                }

            } else if (command == BOOK_SUBJECT) {
                if (splittedInput.Length == 2){
                    Console.WriteLine("------------------ " + splittedInput[1] +  "------------------");

                    for (int index = 0; index < booksArray.GetUpperBound(0); index++) {
                        if (booksArray[index, 1] == splittedInput[1]) {
                            Console.WriteLine("[" + index.ToString() + "]: bookName: " + booksArray[index, 0]);
                        }
                    }
                } else {
                    Console.WriteLine("[Invalid command]: BookSubject needs 2 arguments.");
                }

            } else if (command == EDIT_USER) {
                if (splittedInput.Length == 4){
                    int index = int.Parse(splittedInput[1]);
                    usersArray[index, 0] = splittedInput[2];
                    usersArray[index, 1] = splittedInput[3];
                    Console.WriteLine("User " + splittedInput[1] + " info successfully updated!");

                } else {
                    Console.WriteLine("[Invalid command]: EditUser needs 4 arguments.");
                }

            } else {
                Console.WriteLine("Invalid command!");
            }
        }
    }
}