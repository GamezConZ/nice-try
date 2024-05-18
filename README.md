# Python Quiz Program

A simple quiz application to create and answer multiple-choice and true/false questions. This project showcases fundamental Python skills and is part of my learning journey as a Python developer.

## Features

- **User Roles**: Users can choose to be quiz creators or quiz takers.
- **Question Types**: Supports both multiple-choice and true/false questions.
- **Persistent Storage**: Saves and loads quizzes using JSON files.

## Usage

### Running the Program

1. **Clone the Repository**

   ```bash
   git clone https://github.com/GamezConZ/nice-try.git
   cd nice-try
Run the Program

bash

    python3 main.py

Creating a Quiz

  Run the program and select the option to create questions.
  Follow the prompts to input your questions and save them.

Taking a Quiz

   Run the program and select the option to answer questions.
   Provide the username of the quiz creator to load the saved questions.
   Answer the questions as prompted.

Code Overview

   User class: Stores user data and tracks quiz performance.
   
   Question class: Handles the creation, asking, and evaluation of questions.
   
   create_user(): Initializes user role and data.
   
   create_questions(): Facilitates question creation and saving.
   
   save_questions(): Saves questions to a JSON file.
   
   use_saved_questions(): Loads questions from a JSON file.
   
   main(): Main function to run the program.
   

Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

For any questions or feedback, feel free to reach out.
