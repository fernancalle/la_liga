import sqlite3

db_file = 'spanish_la_liga.db'
conn = sqlite3.connect(db_file)

# Drop existing tables if they exist
conn.execute("DROP TABLE IF EXISTS teams;")
conn.execute("DROP TABLE IF EXISTS matches_22_23;")
conn.execute("DROP TABLE IF EXISTS matches_23_24;")

# Create the 'teams' table
conn.execute('''
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT UNIQUE
);
''')

# Create the 'matches_22_23' and 'matches_23_24' tables with the updated field names
table_creation_query = '''
CREATE TABLE {} (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Div TEXT,
    Date TEXT,
    Time TEXT,
    HomeTeam INTERGER,
    AwayTeam INTERGER,
    FTHG INTEGER,
    FTAG INTEGER,
    FTR TEXT,
    HTHG INTEGER,
    HTAG INTEGER,
    HTR TEXT,
    HS INTEGER,
    "AS" INTEGER,
    HST INTEGER,
    AST INTEGER,
    HF INTEGER,
    AF INTEGER,
    HC INTEGER,
    AC INTEGER,
    HY INTEGER,
    AY INTEGER,
    HR INTEGER,
    AR INTEGER,
    B365H REAL,
    B365D REAL,
    B365A REAL,
    BWH REAL,
    BWD REAL,
    BWA REAL,
    IWH REAL,
    IWD REAL,
    IWA REAL,
    PSH REAL,
    PSD REAL,
    PSA REAL,
    WHH REAL,
    WHD REAL,
    WHA REAL,
    VCH REAL,
    VCD REAL,
    VCA REAL,
    MaxH REAL,
    MaxD REAL,
    MaxA REAL,
    AvgH REAL,
    AvgD REAL,
    AvgA REAL,
    "B365>2.5" REAL,
    "B365<2.5" REAL,
    "P>2.5" REAL,
    "P<2.5" REAL,
    "Max>2.5" REAL,
    "Max<2.5" REAL,
    "Avg>2.5" REAL,
    "Avg<2.5" REAL,
    AHh REAL,
    B365AHH REAL,
    B365AHA REAL,
    PAHH REAL,
    PAHA REAL,
    MaxAHH REAL,
    MaxAHA REAL,
    AvgAHH REAL,
    AvgAHA REAL,
    B365CH REAL,
    B365CD REAL,
    B365CA REAL,
    BWCH REAL,
    BWCD REAL,
    BWCA REAL,
    IWCH REAL,
    IWCD REAL,
    IWCA REAL,
    PSCH REAL,
    PSCD REAL,
    PSCA REAL,
    WHCH REAL,
    WHCD REAL,
    WHCA REAL,
    VCCH REAL,
    VCCD REAL,
    VCCA REAL,
    MaxCH REAL,
    MaxCD REAL,
    MaxCA REAL,
    AvgCH REAL,
    AvgCD REAL,
    AvgCA REAL,
    "B365C>2.5" REAL,
    "B365C<2.5" REAL,
    "PC>2.5" REAL,
    "PC<2.5" REAL,
    "MaxC>2.5" REAL,
    "MaxC<2.5" REAL,
    "AvgC>2.5" REAL,
    "AvgC<2.5" REAL,
    AHCh REAL,
    B365CAHH REAL,
    B365CAHA REAL,
    PCAHH REAL,
    PCAHA REAL,
    MaxCAHH REAL,
    MaxCAHA REAL,
    AvgCAHH REAL,
    AvgCAHA REAL,
    FOREIGN KEY (HomeTeam) REFERENCES teams(team_name),
    FOREIGN KEY (AwayTeam) REFERENCES teams(team_name)
);
'''

# Execute table creation for both seasons
conn.execute(table_creation_query.format('matches_22_23'))
conn.execute(table_creation_query.format('matches_23_24'))

conn.commit()
conn.close()

print("Database structure has been updated to include season-specific tables with correct field names.")
