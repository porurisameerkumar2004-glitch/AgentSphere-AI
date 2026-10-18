
"""Main Flask application for AgentSphere AI."""

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    Response,
)
import csv
import io
import os
from openai import OpenAI
from functools import wraps

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from werkzeug.security import check_password_hash

from database import (
    initialize_database,
    create_user,
    get_user_by_email,
    get_user_by_id,
    get_user_settings,
    update_user_settings,
    save_simulation,
    get_simulation_history,
    get_dashboard_stats,
)
from simulation import run_simulation


app = Flask(__name__)
app.secret_key = os.environ.get(
    "FLASK_SECRET_KEY",
    "local-development-key-change-me",
)

EVENTS = {
    "normal": "Normal Business Conditions",
    "budget_cut": "Budget Cut",
    "demand_surge": "Customer Demand Surge",
    "server_outage": "Server Outage",
    "competitor": "New Competitor",
}

initialize_database()


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "info")
            return redirect(url_for("login"))

        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def home():
    if session.get("user_id"):
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("display_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("Please complete every field.", "error")

        elif len(password) < 8:
            flash("Password must contain at least 8 characters.", "error")

        elif get_user_by_email(email):
            flash("An account with this email already exists.", "error")

        else:
            try:
                create_user(email, password, name)
                flash("Account created. Please log in.", "success")
                return redirect(url_for("login"))

            except Exception:
                app.logger.exception("Registration failed")
                flash(
                    "Registration failed. Check the terminal for details.",
                    "error",
                )

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = get_user_by_email(email)

        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("dashboard"))

        flash("Invalid email or password.", "error")

    return render_template("login.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have logged out.", "success")
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    user_id = session["user_id"]

    return render_template(
        "dashboard.html",
        user=get_user_by_id(user_id),
        preferences=get_user_settings(user_id),
        stats=get_dashboard_stats(),
        history=get_simulation_history(limit=5),
        events=EVENTS,
    )


@app.route("/simulations", methods=["GET", "POST"])
@login_required
def simulations():
    user_id = session["user_id"]

    # Pass preferences to the template to prevent
    # the previous 'preferences is undefined' error.
    preferences = get_user_settings(user_id)
    selected_event = preferences["default_event"]
    result = None

    if request.method == "POST":
        selected_event = request.form.get("event", "normal")

        if selected_event not in EVENTS:
            selected_event = "normal"

        result = run_simulation(selected_event)
        result["event_label"] = EVENTS[selected_event]
        save_simulation(result)

    return render_template(
        "index.html",
        result=result,
        events=EVENTS,
        selected_event=selected_event,
        history=get_simulation_history(),
        preferences=preferences,
        user=get_user_by_id(user_id),
    )


@app.route("/export/csv")
@login_required
def export_csv():
    # Get the saved simulation history.
    history = get_simulation_history()

    # Create CSV content in memory.
    output = io.StringIO()
    writer = csv.writer(output)

    # CSV column headings.
    writer.writerow([
        "Simulation ID",
        "Business Event",
        "CEO Strategy",
        "Date and Time",
    ])

    # Write one row for each saved simulation.
    for item in history:
        writer.writerow([
            item["id"],
            item["event"],
            item["strategy"],
            item["created_at"],
        ])

    # Send the CSV file to the browser.
    return Response(
        "\ufeff" + output.getvalue(),
        mimetype="text/csv; charset=utf-8",
        headers={
            "Content-Disposition":
                'attachment; filename="agentsphere_simulation_history.csv"'
        },
    )

@app.route("/assistant", methods=["GET", "POST"])
@login_required
def assistant():
    answer = None
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if not question:
            flash("Please enter a question.", "error")

        elif len(question) > 2000:
            flash("Keep your question under 2,000 characters.", "error")

        elif not os.environ.get("OPENAI_API_KEY"):
            flash(
                "Set the OPENAI_API_KEY environment variable first.",
                "error",
            )

        else:
            try:
                client = OpenAI()

                response = client.responses.create(
                    model="gpt-5-mini",
                    instructions=(
                        "You are the AgentSphere AI business assistant. "
                        "Explain business simulations, Finance, Sales, "
                        "Marketing, Development, and CEO strategies in "
                        "simple language. Give practical suggestions. "
                        "Do not claim to have read live company records "
                        "unless they are included in the question. "
                        "Explain that simulation figures are illustrative."
                    ),
                    input=question,
                )

                answer = response.output_text

            except Exception:
                app.logger.exception("AI assistant request failed")
                flash(
                    "The AI assistant could not respond. "
                    "Check the API key, account access, and terminal logs.",
                    "error",
                )

    return render_template(
        "chat.html",
        user=get_user_by_id(session["user_id"]),
        preferences=get_user_settings(session["user_id"]),
        question=question,
        answer=answer,
    )


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    user_id = session["user_id"]
    user = get_user_by_id(user_id)
    preferences = get_user_settings(user_id)

    if request.method == "POST":
        name = request.form.get("display_name", "").strip()
        theme = request.form.get("theme", "light")
        default_event = request.form.get("default_event", "normal")

        if not name:
            flash("Display name cannot be empty.", "error")

        elif theme not in {"light", "dark"}:
            flash("Choose a valid appearance.", "error")

        elif default_event not in EVENTS:
            flash("Choose a valid default event.", "error")

        else:
            update_user_settings(
                user_id, name, theme, default_event
            )
            flash("Settings saved successfully.", "success")
            return redirect(url_for("settings"))

    return render_template(
        "settings.html",
        user=user,
        preferences=preferences,
        events=EVENTS,
    )


if __name__ == "__main__":
    app.run(debug=True)
