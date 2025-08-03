from sqlalchemy import create_engine, text


db_connection = "postgresql://Moiseeva:12341@localhost:5432/Homework"
db = create_engine(db_connection)


def test_add_subject():
    with db.connect() as connection:
        transaction = connection.begin()

        try:
            sql = text(
                "INSERT INTO subject(subject_title, subject_id) "
                "VALUES (:subject_title, :subject_id)"
            )
            connection.execute(
                sql,
                {'subject_title': "Skypro", 'subject_id': 16}
            )

            res = connection.execute(
                text(
                    "SELECT subject_title FROM subject "
                    "WHERE subject_id = :id"
                ),
                {"id": 16}
            ).fetchone()

            assert res is not None
            assert res[0] == "Skypro"

        finally:
            transaction.rollback()


def test_edit_subject():
    with db.connect() as connection:
        transaction = connection.begin()

        try:
            sql_insert = text(
                "INSERT INTO subject(subject_title, subject_id) "
                "VALUES (:subject_title, :subject_id)"
            )
            connection.execute(
                sql_insert,
                {'subject_title': "Skypro", 'subject_id': 16}
            )

            sql_update = text(
                "UPDATE subject SET subject_title = :subject_title "
                "WHERE subject_id = :subject_id"
            )
            connection.execute(
                sql_update,
                {'subject_title': "New_subject_title", 'subject_id': 16}
            )

            res = connection.execute(
                text(
                    "SELECT subject_title FROM subject "
                    "WHERE subject_id = :id"
                ),
                {"id": 16}
            ).fetchone()

            assert res is not None
            assert res[0] == "New_subject_title"

        finally:
            transaction.rollback()


def test_delete_subject():
    with db.connect() as connection:
        transaction = connection.begin()

        try:
            sql_insert = text(
                "INSERT INTO subject(subject_title, subject_id) "
                "VALUES (:subject_title, :subject_id)"
            )
            connection.execute(
                sql_insert,
                {'subject_title': "Skypro", 'subject_id': 16}
            )

            sql_delete = text(
                "DELETE FROM subject WHERE subject_id = :subject_id"
            )
            connection.execute(
                sql_delete,
                {'subject_id': 16}
            )

            res = connection.execute(
                text(
                    "SELECT subject_title FROM subject "
                    "WHERE subject_id = :id"
                ),
                {"id": 16}
            ).fetchone()

            assert res is None

        finally:
            transaction.rollback()
