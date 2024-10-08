from types import SimpleNamespace


def dict_fetchall(cursor, many=True):
    columns = [col[0] for col in cursor.description]

    rows = dict_zip(columns=columns, data=cursor.fetchall())

    return rows if many else rows[0] if len(rows) > 0 else None


def dict_zip(columns, data) -> list:
    rows = [
        dict(zip(columns, row)) for row in data
    ]
    return rows