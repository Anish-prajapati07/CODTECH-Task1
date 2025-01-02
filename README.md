Name:Anish Prajapati

Company:CODTECH IT SOLUTIONS

ID: CT08EDO

Domain:Cyber security and Ethical hacking

Duration:December 17th,2024 to january 17th,2025

Mentor:Neela Santhosh Kumar

**Overview of the project**

I developed a Password Strength Checker which is a Python tool designed to evaluate the strength of passwords based on various criteria such as length, complexity, and the presence of special characters. The tool provides feedback to help users create stronger passwords.

**Features**

•	Checks password length

•	Ensures the presence of digits, uppercase, and lowercase letters

•	Verifies the inclusion of special characters

•	Provides feedback on how to strengthen the password

**Code Explanation**

•Function Definition:This line defines a function named checkPassword that takes a single parameter password.

![image](https://github.com/user-attachments/assets/9f3840a8-8feb-4bd7-a908-a7d9ce68b6b6)

**Initializing Counters**

•	upperChars: Counter for uppercase characters in the password.

•	lowerChars: Counter for lowercase characters in the password.

•	specialChars: Counter for special characters in the password.

•	digits: Counter for numeric digits in the password.

•	length: Stores the length of the password using the len() function.

![image](https://github.com/user-attachments/assets/74aafb1d-3f47-436c-bc4a-874d1260c041)

**Checking Minimum Length**

![image](https://github.com/user-attachments/assets/ef52ba2c-8a9b-492b-82d9-e4c837fae3f3)

This checks if the password is shorter than 6 characters. If it is, it prints a message indicating that the password must be at least 6 characters long and exits the function.

**Iterating Through Password Character**

![image](https://github.com/user-attachments/assets/a5806561-6c9c-470f-b5bf-3fe1c0eefb42)


•	This loop iterates over each character in the password.

•	password[i].isupper(): Checks if the character is an uppercase letter.

•	password[i].islower(): Checks if the character is a lowercase letter.

•	password[i].isdigit(): Checks if the character is a digit.

•	If the character is none of the above, it is considered a special character.

•	The respective counters are incremented based on the character type.

**Evaluating Password Strength**

![image](https://github.com/user-attachments/assets/e368b40c-7f94-4e2e-8349-017a53dd3892)

•	This checks if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.

•	If all these conditions are met:

•	If the password length is 10 or more characters, it is considered “strong”.

•	Otherwise, it is considered “medium”.

**Providing Feedback for Missing Requirements**

![image](https://github.com/user-attachments/assets/07fba024-b9a7-4829-b2cb-ac2bd195ec69)


•	If the password does not meet the requirement of having at least one of each character type, this block provides specific feedback about what is missing:

•	If there are no uppercase characters, it prints a corresponding message.

•	If there are no lowercase characters, it prints a corresponding message.

•	If there are no special characters, it prints a corresponding message.

•	If there are no digits, it prints a corresponding message.

**Input and Function Call**

![image](https://github.com/user-attachments/assets/98a3c961-a5fb-4228-9f93-8f22ff5143d9)

•	input("Please enter password: "): Prompts the user to enter a password.

•	checkPassword(password): Calls the checkPassword function with the user’s input.

**Output**
output 1
![image](https://github.com/user-attachments/assets/59e9e81f-c779-409d-a297-b180c8929bb6)

output 2
![image](https://github.com/user-attachments/assets/a3710388-f0af-4208-afbd-87ca8e260198)






