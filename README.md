My Network Tools Project
This is a Python project for my Network Programming class. 
I took one big script and broke it up into different modules to keep it clean and organized.



----------------    How to Get It Ready     ----------------
You need to have Python 3 on your computer.

1. Make a Virtual Environment.
It's best to make a "virtual environment" so any libraries you install don't mess with your computer's main Python setup. 
Go to the project folder in your terminal and type:
python -m venv .venv


2. Turn on the Environment
On Windows:
.\.venv\Scripts\activate

On Mac/Linux:
source .venv/bin/activate

3. Install the One Library We Need This project only needs one extra library to work. With your environment still on, run this:
pip install ntplib
(If you have the requirements.txt file, you can just run pip install -r requirements.txt instead).




----------------    How to Run the Project     ----------------
After you do the setup steps above:

-Make sure you are in the main project folder (the one with main_project.py in it).
-Make sure your virtual environment is still on (you see (.venv)).
-Run this command in your terminal:

python main_project.py
A menu will pop up. Just type a number (1-6) and press Enter to choose a tool.




----------------    What Each Tool Does     ----------------
1. Module A: Show Machine Info
This just prints your computer's name (hostname) and its local IP address.

2. Module B: Run Echo Test
This checks if a server can "echo" (repeat back) a message correctly. It starts a mini-server on your computer, then connects with two fake clients to make sure the server sends back the exact message it received.

3. Module C: Perform SNTP Time Check
This connects to a real time server on the internet (pool.ntp.org) and prints the current, official time.

4. Module D: Start Simple Chat Module
This is a basic chat room. You can choose to be the (S)erver or a (C)lient.




----------------    How to Test It Yourself     ----------------
Run the program (python main_project.py).
Choose 4, then S (for Server).
Pick a port number (like 8800) and press Enter. The server is now running and waiting.
Open a brand new, separate terminal window.
In the new window, turn on the virtual environment again (.\.venv\Scripts\activate).
Run the program again (python main_project.py).
This time, choose 4, then C (for Client).
Type in a username and the same port (8800).
Now you can type messages in the client window, and they will show up in the server window!

5. Module E: Settings and Error Handling Demo
You don't "use" this one. It just runs a quick demo that prints out different socket settings (like timeout and buffer size) and proves that the code can handle common network errors (like "Connection Refused").

6. Exit
Closes the program.

Note: Any messages from the chat room (Module D) are automatically saved to the chat_log.txt file.
