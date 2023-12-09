import warnings
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

# Snowflake connection parameters
snowflake_account = 'kg28325.ap-southeast-1.snowflakecomputing.com'
snowflake_user = 'dasariravi'
snowflake_password = 'Ravi0011'
snowflake_warehouse = 'my_wh'

# Suppress DeprecationWarning
warnings.simplefilter("ignore", category=exc.RemovedIn20Warning)

# SQLAlchemy connection string
connection_string = (
    f'snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/'
    f'?warehouse={snowflake_warehouse}&account={snowflake_account}'
)

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Execute a Snowflake SQL query
result = session.execute("SELECT CURRENT_DATE()").fetchone()
print(f"Current date in Snowflake: {result[0]}")

# Close the session
session.close()
