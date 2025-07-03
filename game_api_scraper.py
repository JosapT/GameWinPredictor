

def get_r6siege_profile(username):
    """
    Returns the R6 Siege profile URL for a given username.
    
    :param username: The username of the player.
    :return: The URL to the player's R6 Siege profile.
    """
    if not username:
        raise ValueError("Username cannot be empty.")
    
    # Construct the URL for the R6 Siege profile

    base_link_r6 = f"https://r6.tracker.network/r6siege/profile/ubi/{username}/overview"

    return base_link_r6