# AgentSphere-AI
AgentSphere AI — Multi-Agent Corporation: Simulated AI Organization
AgentSphere AI is a Flask-based web application that simulates a virtual company operated by multiple role-based agents. Each agent represents a department—such as Finance, Marketing, Sales, or Software Development—and contributes recommendations when the company faces a business challenge. A CEO agent combines those recommendations into a proposed strategy, and the application displays the simulated business results.
Note: This project is a business-simulation and learning tool. Its figures and recommendations are illustrative and should not be treated as guaranteed predictions for real businesses.

The project is intended for learning and demonstrating multi-agent collaboration, business simulation, and automated decision-support workflows. All business metrics and simulation outcomes are illustrative and should not be treated as real-world forecasts.
Table of Contents
- Project Overview
- Objectives
- Features
- How It Works
- Technology Stack
- Project Structure
- Prerequisites
- Installation and Setup
  - 1. Clone the Repository
  - 2. Create a Virtual Environment
  - 3. Install Dependencies
  - 4. Configure the Database
  - 5. Configure the Optional AI Assistant
  - 6. Run the Application
- Database Configuration
- Business Scenarios
- CSV Export
- Security Notes
- Troubleshooting
- Security Notes
- Future Enhancements
- Contributing
- License
Project Overview
Organizations make decisions across several departments. A finance decision can affect marketing budgets, a technical outage can affect sales, and a competitor can affect demand. AgentSphere AI provides a virtual environment for exploring these relationships.

Users can run business scenarios, review department recommendations, inspect the CEO strategy, and review saved simulation history. If configured, the optional AI Business Assistant can answer general questions about business strategies and the agents.
Objectives
- Demonstrate collaboration between multiple role-based agents.
- Simulate common business events in a controlled environment.
- Show how decisions can affect budget, revenue, expenses, demand, and productivity.
- Save and review simulation history.
- Export history to CSV for spreadsheet analysis.
- Provide an optional conversational assistant for business-related questions.
Features
The following features describe the intended application. Availability depends on the features implemented in your current codebase.
- User registration and login — account access for application users.
- Company dashboard — presents simulated business metrics.
- Role-based agents — Finance, Developer, Marketing, Sales, and CEO agents.
- Business scenario simulation — tests selected events and calculates illustrative outcomes.
- CEO strategy selection — combines department recommendations into a proposed strategy.
- Simulation history — stores previous simulation records.
- CSV export — downloads simulation history as a spreadsheet-compatible CSV file.
- Settings page — manages supported user preferences.
- Optional AI Business Assistant — uses the OpenAI API when configured.
- Optional extensions — scenario comparison, risk alerts, PDF reports, and agent negotiation can be added as future features.
How It Works
1. The user signs in and opens the application dashboard.
2. The user selects a business scenario, such as a budget cut or server outage.
3. The simulation initializes the company's example metrics.
4. Each department agent analyzes the scenario and returns a recommendation.
5. The CEO agent selects a strategy based on those recommendations.
6. The simulation updates the example metrics and calculates the result.
7. The application displays the outcome and can save it to the database.
8. The user can review saved history and export it to CSV if that feature is enabled.
Agent Responsibilities
Agent	Responsibility
Finance Agent	Reviews costs, expenses, and budget-related decisions.
Developer Agent	Considers technical issues and software productivity.
Marketing Agent	Considers customer demand and marketing responses.
Sales Agent	Focuses on sales opportunities and demand.
CEO Agent	Reviews recommendations and selects an overall strategy.


Implementation note: If the agents use fixed rules in agents.py, describe them as rule-based agents rather than claiming they are all powered by a large language model. The optional AI assistant is a separate integration.
Technology Stack
Technology	Purpose
Python	Agent logic and simulation calculations
Flask	Web framework and application routes
HTML	Web page structure
CSS	User interface styling
JavaScript	Browser-side interactions
MySQL or SQLite	Persistent storage, depending on configuration
mysql-connector-python	Python connection to MySQL, if MySQL is used
OpenAI API (optional)	Conversational AI assistant, if configured
CSV	Exporting simulation records


Project Structure
A typical project structure may look like this. Your actual repository may have additional or differently named files.




AgentSphereAI/
├── app.py
├── database.py
├── agents.py
├── simulation.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── settings.html
│   └── chat.html                 # optional AI assistant
└── static/
    ├── style.css            # if used



    
Do not commit your virtual environment (venv/), API keys, passwords, or private database files to GitHub.
Prerequisites

Install the following:
- Python 3.10 or a compatible version supported by your dependencies.
- Git, if cloning the repository.
- VS Code or another Python editor.
- A database appropriate to your current configuration:
  - SQLite for a local file-based setup, or
  - MySQL Server for a MySQL setup.
- An OpenAI API key only if the optional AI assistant is implemented and enabled.
Installation and Setup
1. Clone the Repository
Replace YOUR-USERNAME with your GitHub username and use your actual repository URL.
git clone https://github.com/porurisameerkumar2004-glitch/AgentSphere-AI.git
cd AgentSphereAI
If you have not published the project to GitHub, open the existing project folder instead.
2. Create a Virtual Environment
Windows PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
If PowerShell blocks activation, use Command Prompt:
venv\Scripts\activate.bat
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
If requirements.txt is present:
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
If the project uses MySQL, ensure the requirements include:
mysql-connector-python
If the optional OpenAI assistant is implemented, ensure its SDK is included in the requirements file (for example, openai). Keep existing dependencies required by the application.
4. Configure the Database
Use only the configuration matching your implementation.
Option A: SQLite
SQLite stores data in a local database file and does not require a separate database server. Check database.py for the configured file name and follow the initialization method used by the application.
Option B: MySQL
1. Install and start MySQL Server.
2. Create a database in MySQL Workbench or a MySQL client:
CREATE DATABASE agentsphere_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
3. Configure the environment variables expected by your database.py.
For example, if your code reads these variable names, set them in Windows PowerShell:
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_USER="root"
$env:DB_NAME="agentsphere_db"
$env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
Install the connector if needed:
python -m pip install mysql-connector-python
Important: The database schema and SQL queries in database.py must be MySQL-compatible. Creating a database alone does not convert SQLite queries or migrate existing SQLite records. Back up the old database and migrate the required tables and records before removing or abandoning the original data. Use a dedicated database user with limited permissions for deployments.
5. Configure the Optional AI Assistant
Skip this section if the AI Business Assistant is not implemented.

If the application uses the OpenAI Python SDK, install the dependency if necessary:
python -m pip install openai
Set your API key in the current PowerShell terminal:
$env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
Use the model configured in your code and ensure your API account has access. API usage may incur charges. Never hard-code the key or commit it to GitHub.
6. Run the Application
If app.py is the Flask entry point:
python app.py
Open the local URL printed by Flask. It is commonly:

http://127.0.0.1:5000/login

Use Flask's development server for local development only, not as a production deployment server.
Database Configuration
The database layer is typically managed in database.py.

Common responsibilities include:
- Creating required tables.
- Creating and retrieving user records.
- Reading and updating user preferences.
- Saving simulation results and recommendations.
- Retrieving simulation history.
For a multi-user deployment, associate each simulation with its owner and filter history and CSV exports by the authenticated user's ID. Do not expose one user's private records to another user.
Business Scenarios
The simulation may include scenarios such as:
- Budget cut: the company has to manage a reduced budget.
- Demand surge: customer demand increases.
- Server outage: a technical problem affects operations or productivity.
- Competitor entry: a competitor puts pressure on revenue or demand.
- Normal operation: the company runs without a special event.
The exact scenarios and calculations are defined in simulation.py and agents.py. Update this list if your implementation supports different events.
CSV Export
If the CSV export route has been implemented, users can download saved simulation history as a .csv file and open it in Excel, LibreOffice Calc, or another spreadsheet application.

A typical export may include:
- Simulation ID
- Business event
- CEO strategy
- Date and time
The actual columns depend on the export code. For a multi-user application, export only records the signed-in user is authorized to access.
Security Notes
- Store passwords as secure hashes; never store plain-text passwords.
- Keep database passwords and API keys in environment variables or a suitable secrets manager.
- Add .env, venv/, and local database files to .gitignore where appropriate.
- Validate user input and use parameterized SQL queries.
- Protect forms against CSRF where relevant.
- Use authorization checks for private pages and per-user data.
- Do not expose database errors, secrets, or stack traces to end users in production.
- Use HTTPS and a production-ready WSGI server when deploying.
- Treat AI output as untrusted and verify important business decisions.
- Use a dedicated, least-privilege MySQL account for the application rather than the root account.
Troubleshooting
Problem	Things to check
ModuleNotFoundError	Activate the virtual environment and install requirements.txt.
MySQL connection refused	Confirm MySQL Server is running and host/port are correct.
MySQL access denied	Check username, password, and database permissions.
Unknown database	Create the database or correct DB_NAME.
Table does not exist	Run the application's initialization/migration process.
SQLite SQL syntax error after switching	Convert query placeholders and table definitions to MySQL syntax.
Flask template or endpoint error	Check template paths, route names, and url_for() calls.
AI assistant cannot respond	Check the API key, SDK, model access, network connection, and terminal logs.
CSV export is empty	Confirm simulations are being saved and the export queries the intended user's records.


Future Enhancements
Possible extensions include:
- Side-by-side scenario comparison.
- Risk alerts and event notifications.
- Downloadable PDF business reports.
- Agent negotiation and conflict resolution.
- Charts for historical performance.
- More realistic, configurable company metrics.
- Audit logs and CEO approval workflows.
- Automated tests and deployment configuration.
Contributing
1. Fork the repository.
2. Create a branch for your change.
3. Make and test your changes.
4. Commit your work with a descriptive message.
5. Open a pull request explaining the change.
License
No license is specified by this README. Add a LICENSE file and update this section if you choose to distribute the project under a particular open-source license.
