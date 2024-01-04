import pandas as pd
import sqlite3

def sanitize_column_names(df):
    """Sanitize column names to remove special characters and spaces."""
    df.columns = [re.sub(r'[^a-zA-Z0-9]', '_', col) for col in df.columns]
    return df

def get_team_id(conn, team_name):
    """Retrieve or insert team_id for a given team name."""
    conn.execute("INSERT OR IGNORE INTO teams (team_name) VALUES (?)", (team_name,))
    conn.commit()
    team_id = conn.execute("SELECT team_id FROM teams WHERE team_name = ?", (team_name,)).fetchone()[0]
    return team_id

def load_csv_to_db(csv_file_path, db_file_path, season):
    # Read CSV data into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)

    # Define the table name based on the season
    table_name = f"matches_{season}"

    # Convert team names to team IDs
    df['HomeTeam'] = df['HomeTeam'].apply(lambda x: get_team_id(conn, x))
    df['AwayTeam'] = df['AwayTeam'].apply(lambda x: get_team_id(conn, x))

    # Insert data into the database
    df.to_sql(table_name, conn, if_exists='append', index=False)

    # Close the connection
    conn.close()

# Paths to the CSV files
csv_file_1 = '/Users/fernandocalle/Desktop/portfolio/la_liga/laliga_22_23.csv'
csv_file_2 = '/Users/fernandocalle/Desktop/portfolio/la_liga/laliga_23_24.csv'

# Database file path
db_file = 'spanish_la_liga.db'

# Load data from both CSV files into separate season-specific tables
load_csv_to_db(csv_file_1, db_file, '22_23')
load_csv_to_db(csv_file_2, db_file, '23_24')

print("Data from both CSV files for the updated seasons has been successfully loaded into separate season-specific tables.")