from enum import Enum

class QueryTypes(Enum):
    SELECT = "SELECT"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class QueryBuilder:
    def __init__(self):
        self.table = None
        self.query_type = None
        self.columns = None
        self.select_fields = "*"
        self.joins = []
        self.where_conditions = []
        self.group_by_columns = []
        self.order_by_clause = None
        self.limit_clause = None

    def select(self, fields):
        self.select_fields = ", ".join(fields) if fields else "*"
        return self

    def join(self, join_type, table, on_condition):
        self.joins.append(f"{join_type} JOIN {table} ON {on_condition}")
        return self

    def where(self, condition):
        self.where_conditions.append(condition)
        return self

    def group_by(self, columns):
        self.group_by_columns = columns
        return self

    def order_by(self, column, direction="ASC"):
        self.order_by_clause = f"ORDER BY {column} {direction}"
        return self

    def limit(self, limit_value):
        self.limit_clause = f"LIMIT {limit_value}"
        return self

    def build(self, query_type, table, columns=None):
        self.query_type = query_type.value
        self.table = table
        self.columns = columns
        query = ""

        if self.query_type == QueryTypes.SELECT.value:
            query = f"{self.query_type} {self.select_fields} FROM {self.table}"

            if self.joins:
                query += " " + " ".join(self.joins)
            if self.where_conditions:
                query += " WHERE " + " AND ".join(self.where_conditions)
            if self.group_by_columns:
                query += f" GROUP BY {', '.join(self.group_by_columns)}"
            if self.order_by_clause:
                query += f" {self.order_by_clause}"
            if self.limit_clause:
                query += f" {self.limit_clause}"

        elif self.query_type == QueryTypes.INSERT.value:
            if not self.columns:
                raise Exception("There are no columns to insert")

            columns = ", ".join(self.columns.keys())
            values_placeholder = ", ".join(["%s"] * len(self.columns))
            query = f"INSERT INTO {self.table} ({columns}) VALUES ({values_placeholder})"

        elif self.query_type == QueryTypes.UPDATE.value:
            if not self.columns:
                raise Exception("There are no columns to update")

            set_clause = ", ".join([f"{col} = %s" for col in self.columns.keys()])
            query = f"UPDATE {self.table} SET {set_clause}"
            if self.where_conditions:
                query += " WHERE " + " AND ".join(self.where_conditions)


        elif self.query_type == QueryTypes.DELETE.value:
            query = f"DELETE FROM {self.table}"
            if self.where_conditions:
                query += " WHERE " + " AND ".join(self.where_conditions)

        return query