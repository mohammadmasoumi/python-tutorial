namespace HelloWorld
{
    class Program
    {

        // commands
        const string ADD_BOOK = "ADDBOOK"; 
        const string ADD_STUDENT = "ADDSTUDENT"; 

        const string EXIT = "exit";


        static void Main(string[] args)
        {   

            string inputString, command;
            bool isFinished = false;

            List<string> books = new List<string>();
            List<string> students = new List<string>();
            
            while (!isFinished) 
            {
                inputString = Console.ReadLine() ?? "";

                string[] splittedInput =  inputString.Split(" ");
                command = splittedInput[0];

                Console.WriteLine("inputString: " + inputString);  // DEBUG
                Console.WriteLine("command: " + command);  // DEBUG

                if (command == EXIT){
                    break;
                } else if (command == ADD_BOOK){
                    Console.WriteLine("I found ADDBOOK command");
                }

            }
        }
    }
}