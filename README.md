# AgentSphere-AI
AgentSphere AI — Multi-Agent Corporation: Simulated AI Organization
AgentSphere AI is a web application that simulates a company operated by multiple software agents. Each agent represents a business department, such as Finance, Marketing, Sales, or Development. The agents analyze a simulated business situation and provide recommendations that a CEO agent can use to select a strategy.

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
- Database Configuration
- Running the Application
- Example Simulation Scenarios
- CSV Export
- AI Business Assistant
- Troubleshooting
- Security Notes
- Future Enhancements
- Contributing
- License
Project Overview
Organizations make decisions across multiple departments. A finance team may focus on costs, marketing may focus on demand, sales may focus on revenue, and developers may focus on technical stability. AgentSphere AI models these different responsibilities in one virtual company.

A user selects a business event, such as a budget cut, competitor pressure, a demand surge, or a server outage. Department agents analyze the event, produce recommendations, and the CEO agent selects a strategy. The application then displays the simulated company metrics and can store the results for later review.
Objectives
- Demonstrate how multiple agents can work together on a shared problem.
- Simulate business events in a controlled environment.
- Show the effect of a scenario on metrics such as budget, revenue, expenses, demand, and productivity.
- Store and review previous simulation results.
- Provide a foundation for an optional conversational AI assistant.
- Practice web development, database integration, and reporting.
Features
The following features are part of the intended project scope. The features actually available depend on the code implemented in your repository and the configuration of any external services.
- User registration and login — account access, if authentication routes are implemented.
- Company dashboard — display simulated company metrics and results.
- Department agents — Finance, Developer, Marketing, and Sales agents provide role-specific recommendations.
- CEO strategy selection — the CEO agent combines recommendations into a response strategy.
- Business scenario simulation — test events such as budget cuts, competitor pressure, demand surges, and server outages.
- Simulation history — save and review previous runs.
- CSV export — download simulation history as a spreadsheet-compatible CSV file, if the export route is implemented.
- AI Business Assistant — ask questions about business strategies and agent responsibilities when an AI provider is configured.
- User settings — manage supported application preferences, if implemented.
How It Works
1. The user opens the application and selects a business scenario.
2. The application loads the initial simulated company state.
3. Each department agent analyzes the state and selected event.
4. The CEO agent reviews the recommendations and selects a strategy.
5. The simulation applies the scenario and agent changes to the company metrics.
6. The application displays the results and, when configured, saves them to the database.
7. The user can review saved history or export it to CSV if those features are implemented.
Technology Stack
Technology	Purpose
Python	Simulation logic and agent behavior
Flask	Web server and application routes
HTML	Page structure
CSS	User interface styling
JavaScript	Optional interactive page behavior
MySQL	Target relational database for application data
SQLite	May be used by earlier versions of the project
mysql-connector-python	Python connection to MySQL
OpenAI API (optional)	Powers a conversational assistant if integrated and configured
CSV	Export format for simulation history


Project Structure
A typical project structure may look like this. Your actual repository may have additional or differently named files.
AgentSphereAI/
├── app.py
├── database.py
├── agents.py
├── simulation.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── settings.html
│   └── chat.html
├── static/
│   ├── style.css
│   └── dashboard.css
└── .gitignore
- app.py — creates the Flask application and defines routes.
- database.py — connects to the database and contains database operations.
- agents.py — defines the department agents and CEO decision logic.
- simulation.py — runs business scenarios and calculates simulated outcomes.
- templates/ — contains the HTML templates.
- static/ — contains CSS, JavaScript, and other static assets.
- requirements.txt — lists Python package dependencies.
Prerequisites
Install the following software:
- Python 3.10 or a compatible version supported by your dependencies.
- Git, if cloning the repository.
- Visual Studio Code or another Python editor.
- MySQL Server if using the MySQL configuration.
- MySQL Workbench (optional) for managing the database graphically.
Installation and Setup
1. Clone the repository
Replace the example URL with the URL of your own GitHub repository.
git clone https://github.com/YOUR-USERNAME/AgentSphereAI.git
cd AgentSphereAI
If you already have the project on your computer, open its folder in VS Code instead.
2. Create a virtual environment
Windows PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
If PowerShell blocks activation, use Command Prompt:
venv\Scripts\activate.bat
macOS or Linux:
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
If the repository has a requirements.txt file:
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
If MySQL is used, make sure the requirements include:
mysql-connector-python
If the optional AI assistant uses OpenAI, its required SDK must also be included in requirements.txt.
Database Configuration
MySQL setup
1. Install and start MySQL Server.
2. Connect using MySQL Workbench or the MySQL command-line client.
3. Create a database:
CREATE DATABASE agentsphere_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
4. Configure the connection using the environment variable names expected by your database.py.
For example, if your code reads these variables, set them in Windows PowerShell:
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_USER="root"
$env:DB_NAME="agentsphere_db"
$env:DB_PASSWORD="your_mysql_password"
Replace your_mysql_password with your own MySQL password. These variables apply only to the current terminal session. Set them again when you open a new terminal.

Important: The environment variable names and database schema must match your code. Creating the database alone does not create all required tables. Ensure initialize_database() or your migration/setup script creates the tables used by the application.
Existing SQLite data
Changing the connection does not automatically copy data from an existing SQLite database such as corporation.db. Back up the SQLite file, create matching MySQL tables, migrate the records, and verify them before removing or abandoning the old database.
Running the Application
After installing dependencies and configuring the database, run:
python app.py
Open the local address printed by Flask. In a typical development setup, it is:

http://127.0.0.1:5000

If your application uses a different port, open the address shown in the terminal.
Example Simulation Scenarios
The project may include scenarios such as:
- Budget cut — simulate a reduction in available budget and explore cost-control recommendations.
- Demand surge — simulate increased customer demand and review the company's response.
- Server outage — simulate a technical disruption and observe its effect on productivity or revenue.
- Competitor pressure — simulate a competitor affecting demand or revenue.
The available scenarios and the exact calculations are defined in simulation.py and agents.py.
CSV Export
If the CSV export route is implemented, users can download saved simulation history as a .csv file and open it in spreadsheet software such as Microsoft Excel or LibreOffice Calc.

The export should include only records the signed-in user is authorized to access. Confirm the route name and fields in your code; they may differ from the example project structure.
AI Business Assistant
The optional AI Business Assistant can answer questions about business scenarios, strategies, and agent roles. If it uses an external AI API:
1. Install the required SDK.
2. Create an API key with the provider.
3. Set the key as an environment variable using the name expected by your code.
4. Keep the key private and out of source control.
5. Handle API errors and be aware that API usage may incur charges.
Unless the application explicitly passes saved simulation data to the AI model, do not assume that the assistant can see or analyze the database records.
Troubleshooting
- ModuleNotFoundError — activate the project's virtual environment and install requirements.txt.
- MySQL connection error — confirm MySQL Server is running, the host and port are correct, the database exists, and credentials are valid.
- Table does not exist — run the database initialization or migration procedure.
- Flask BuildError — check that each url_for() endpoint matches a function name in app.py.
- Template variable is undefined — ensure the Flask route passes the variable expected by the HTML template.
- CSS is not loading — verify the CSS file is inside the static/ directory and referenced using Flask's url_for('static', filename='...').
- AI assistant errors — verify the API key, provider access, model availability, network access, and application logs.
Security Notes
- Never commit database passwords, API keys, or other secrets to GitHub.
- Use environment variables or an appropriate secret manager for credentials.
- Use password hashing for account passwords; do not store plain-text passwords.
- Use parameterized SQL queries rather than building queries from user input.
- Add CSRF protection to state-changing web forms.
- Restrict simulation history and exports to the appropriate signed-in user.
- Use a dedicated MySQL account with limited privileges instead of using the root account in production.
- Disable Flask debug mode in production.
- Treat AI-generated suggestions as informational and verify important decisions.
Future Enhancements
Possible improvements include:
- Compare results from multiple scenarios.
- Add a CEO approval workflow for proposed strategies.
- Add risk alerts and performance charts.
- Generate downloadable PDF reports.
- Record agent-to-agent discussions and negotiations.
- Add more configurable scenarios and evaluation metrics.
- Add automated tests and database migrations.
- Connect the assistant to selected simulation records with appropriate access controls.
Contributing
1. Fork the repository.
2. Create a branch for your change.
3. Make and test your changes.
4. Commit with a descriptive message.
5. Open a pull request describing the change.
Before submitting, confirm that secrets and local database files are not included in the commit.
License
No license has been specified here. Add a LICENSE file and update this section if you choose to publish the project under an open-source license.