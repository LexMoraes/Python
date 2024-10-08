import sqlite3
from types import SimpleNamespace

import requests

import util
from db.database import ConnectionSQLite
from model import Contact


class AgendaActions:

    @staticmethod
    def get_zip_code(zip_code: str):
        api_url = f"https://viacep.com.br/ws/{zip_code}/json/"
        response = requests.get(url=api_url)
        data = response.json()

        if 'erro' in data:
            return None

        return data

    @staticmethod
    def save_contact(contact: Contact):
        _connection_sqlite = ConnectionSQLite()
        _conn = _connection_sqlite.connect()

        if not _conn:
            return _conn
        # Inserts a contact into the database.
        try:
            cursor = _conn.cursor()
            _script = """
            INSERT INTO contacts (name, email, cell_phone, zip_code, street, neighborhood, city, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """
            _values = (
                contact.name,
                contact.email,
                contact.cell_phone,
                contact.zip_code,
                contact.street,
                contact.neighborhood,
                contact.city,
                contact.state
            )
            cursor.execute(_script, _values)
            _conn.commit()

            print("Contact saved successfully.")
            return "Contact saved successfully."
        except sqlite3.Error as e:
            print(f"Error inserting contact: {e}")
            return f"Error inserting contact: {e}"

    @staticmethod
    def list_contacts() -> list:
        _connection_sqlite = ConnectionSQLite()
        _conn = _connection_sqlite.connect()

        cursor = _conn.cursor()

        _script = "SELECT * FROM contacts;"

        cursor.execute(_script)

        fetchall = util.dict_fetchall(cursor=cursor, many=True)

        contacts = [SimpleNamespace(**row) for row in fetchall]

        _conn.close()

        return contacts

