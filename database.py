
"""Database operations for AgentSphere AI."""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

from werkzeug.security import generate_password_hash

DATABASE = Path(__file__).with_name("corporation.db")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS user_settings (
                user_id INTEGER PRIMARY KEY,
                theme TEXT NOT NULL DEFAULT 'light',
                default_event TEXT NOT NULL DEFAULT 'normal',
                FOREIGN KEY (user_id) REFERENCES users(id)
                    ON DELETE CASCADE
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS simulations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event TEXT NOT NULL,
                strategy TEXT NOT NULL,
                company_state TEXT NOT NULL,
                recommendations TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


def create_user(email, password, display_name):
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO users (email, password_hash, display_name)
            VALUES (?, ?, ?)
            """,
            (
                email.strip().lower(),
                generate_password_hash(password),
                display_name.strip(),
            ),
        )

        user_id = cursor.lastrowid

        connection.execute(
            "INSERT INTO user_settings (user_id) VALUES (?)",
            (user_id,),
        )

    return user_id


def get_user_by_email(email):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT id, email, password_hash, display_name
            FROM users WHERE email = ?
            """,
            (email.strip().lower(),),
        ).fetchone()

    return dict(row) if row else None


def get_user_by_id(user_id):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT id, email, display_name
            FROM users WHERE id = ?
            """,
            (user_id,),
        ).fetchone()

    return dict(row) if row else None


def get_user_settings(user_id):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT theme, default_event
            FROM user_settings WHERE user_id = ?
            """,
            (user_id,),
        ).fetchone()

    if row:
        return dict(row)

    return {"theme": "light", "default_event": "normal"}


def update_user_settings(user_id, display_name, theme, default_event):
    with get_connection() as connection:
        connection.execute(
            "UPDATE users SET display_name = ? WHERE id = ?",
            (display_name.strip(), user_id),
        )

        connection.execute("""
            INSERT INTO user_settings
                (user_id, theme, default_event)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                theme = excluded.theme,
                default_event = excluded.default_event
        """, (user_id, theme, default_event))


def save_simulation(result):
    with get_connection() as connection:
        connection.execute("""
            INSERT INTO simulations (
                event, strategy, company_state,
                recommendations, created_at
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            result["event"],
            result["strategy"]["decision"],
            json.dumps(result["company"]),
            json.dumps(result["recommendations"]),
            datetime.now().isoformat(timespec="seconds"),
        ))


def get_simulation_history(limit=None):
    query = """
        SELECT id, event, strategy, created_at
        FROM simulations ORDER BY id DESC
    """
    parameters = ()

    if limit is not None:
        query += " LIMIT ?"
        parameters = (int(limit),)

    with get_connection() as connection:
        rows = connection.execute(query, parameters).fetchall()

    return [dict(row) for row in rows]


def get_dashboard_stats():
    with get_connection() as connection:
        total = connection.execute(
            "SELECT COUNT(*) FROM simulations"
        ).fetchone()[0]

        latest = connection.execute("""
            SELECT company_state, event, created_at
            FROM simulations ORDER BY id DESC LIMIT 1
        """).fetchone()

    metrics = {
        "budget": 0,
        "revenue": 0,
        "expenses": 0,
        "profit": 0,
        "productivity": 0,
        "demand": 0,
    }

    latest_event = None
    latest_time = None

    if latest:
        metrics.update(json.loads(latest["company_state"]))
        latest_event = latest["event"]
        latest_time = latest["created_at"]

    return {
        "total_simulations": total,
        "metrics": metrics,
        "latest_event": latest_event,
        "latest_time": latest_time,
    }
