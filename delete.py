import pyodbc
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Database connection details
server = 'mcruebs04.isad.isadroot.ex.ac.uk'
database = 'BEMM459_GroupR'
username = 'GroupR'
password = 'YuhH722*Ny'

# Establish database connection
cnxn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = cnxn.cursor()

# Schema name (adjust if your tables are under a different schema)
schema_name = 'dbo'

# List of tables in the order they should be cleared, considering foreign key constraints
# Ensure the table names are correct and exist in your database.
# This list should be in reverse order of table creation due to FK dependencies.
tables_to_clear = [
    'Reservation',
    'RoyaltyManagement',
    'CopyrightClaims',
    'CollaborationTermsOfAgreement',  # Added missing comma
    'MusicTrackCatalogue',
    'Clients',
    'Composers'
]

# Disable foreign key constraint check
cursor.execute("EXEC sp_MSforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT ALL'")
cnxn.commit()

# Clear all tables
for table in tables_to_clear:
    try:
        cursor.execute(f"DELETE FROM {schema_name}.{table}")
        cnxn.commit()
        print(f"Table {table} cleared successfully.")
    except pyodbc.Error as e:
        print(f"Error clearing table {table}: {e}")

# Re-enable foreign key constraint check
cursor.execute("EXEC sp_MSforeachtable 'ALTER TABLE ? WITH CHECK CHECK CONSTRAINT ALL'")
cnxn.commit()

# Close the cursor and connection
cursor.close()
cnxn.close()





