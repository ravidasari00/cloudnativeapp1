import warnings
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

# Snowflake connection parameters
snowflake_account = 'kg28325.ap-southeast-1.snowflakecomputing.com'
snowflake_user = 'dasariravi'
snowflake_password = 'Ravi0011'
snowflake_warehouse = 'my_wh'
snowflake_database = 'my_db'  # Replace with your actual database name
snowflake_schema = 'public'      # Replace with your actual schema name
snowflake_table = 'employee'        # Replace with your actual table name

# Suppress DeprecationWarning
warnings.simplefilter("ignore", category=exc.RemovedIn20Warning)

# SQLAlchemy connection string
connection_string = (
    f'snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/'
    f'?warehouse={snowflake_warehouse}&account={snowflake_account}'
    f'&database={snowflake_database}&schema={snowflake_schema}'
)

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Execute a Snowflake SQL query to fetch data from the table
query = f"SELECT * FROM {snowflake_table}"
result = session.execute(query).fetchall()

# Display the result
for row in result:
    print(row)

# Close the session
session.close()
