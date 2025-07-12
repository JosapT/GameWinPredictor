import pandas as pd


def get_nba_data():
    """
    Fetches NBA game data from a CSV file and returns it as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame containing NBA game data.
    """
    try:
        df = pd.read_csv('nba_games.csv', index_col=0)
        df = df.sort_values("date")
        df = df.reset_index(drop=True) #change index to be sequential

        #deleting extra columns that are not needed
        del df["mp.1"]
        del df["mp_opp.1"]
        del df["index_opp"]

        #returns the dataframe with the game data
        return df
    
    except FileNotFoundError:
        print("The file 'nba_games.csv' does not exist. Please check the file path.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found


def add_target(team):
    team["target"] = team["won"].shift(-1)
    return team


def clean_team_data():
    """
    Cleans the team data by adding a target column and removing unnecessary columns.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame with team data.
    """
    df = get_nba_data()
    
    # Adding target column
    df = add_target(df)
    
    
    return df





