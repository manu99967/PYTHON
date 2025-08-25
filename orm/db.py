

import psycopg
from psycopg_pool import ConnectionPool

class PG:

    def __init__(self):
        self.credentials = (
            "host=aws-0-ap-south-1.pooler.supabase.com "
            "dbname=postgres "
            "user=postgres.riwswfjumjztqurzzask "
            "password=www.proxynova.com999 "
            "port=5432"
        )

        self.pool = ConnectionPool(
            conninfo=self.credentials,
            min_size=1,
            max_size=5,
            timeout=300,
            open=True
        )

    def pg_query(self, query, params=()):
        # should execute our query and return any results
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                result = None
                try:
                    result = cur.fetchall()
                except Exception:
                    pass
                conn.commit()
                return result
