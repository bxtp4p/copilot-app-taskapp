
# Task App

This is a simple task app that allows you to create, read, update, and delete tasks. It is a simple MVC application that uses a SQLite database to store tasks. The application is written in Python and uses the Flask web framework.

This app is primarily used for GitHub Copilot prompt engineering exercises. It is not intended to be a production-ready application.

## Getting Started

To get started with the task app, follow these steps:

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/bxtp4p/copilot-app-taskapp.git
   ```

2. Navigate to the project root directory:

   ```sh
   cd github-copilot-prompt-engineering-exercises
   ```

3. Create a virtual environment:

   ```sh
   python3 -m venv venv
   ```

4. Activate the virtual environment:


   - On Windows:

     ```sh
     .\venv\Scripts\Activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

5. Install the dependencies:

      ```sh
      pip install -r requirements.in
      ```

6. From the [src](./src) directory, run the following command to start the task app:

   ```sh
   python3 app.py
   ```

7. Open a web browser and navigate to `http://localhost:5000` to view the task app.
