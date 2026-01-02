from typing import Any, Tuple, List

def validate_user(db: Any, username: str, password: str) -> bool:
    cursor = db.cursor()
    cursor.execute("""
                SELECT
                    username, password
                FROM
                    Users
                WHERE
                    username = %s AND password = %s
                """, (username, password))
    get_items = cursor.fetchall()
    if len(get_items) > 0:
        return True #This username and password exists in the database for the same record.
    return False #This username and passowrd aren't present inside the database.

def check_if_user_exists(db: Any, username: str) -> bool:
    cursor: Any = db.cursor()
    cursor.execute("""
                SELECT
                    username
                FROM
                    users
                WHERE
                    username = %s
                    """, (username,))
    data: List[Tuple[str]] = cursor.fetchall()
    if len(data) > 0:
        return True
    return False