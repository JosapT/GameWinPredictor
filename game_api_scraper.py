import os
import requests
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv


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


def get_r6siege_kd(profile):
    """
    Returns the K/D ratio from the R6 Siege profile.
    
    :param profile: The URL to the player's R6 Siege profile.
    :return: The K/D ratio as a string.
    """
    if not profile:
        raise ValueError("Profile URL cannot be empty.")
    
    # Extract the K/D ratio from the profile page
    try:
        load_dotenv()
        headers = {
            "TRN-Api-Key": os.getenv("TRACKER_API_KEY"),
        }
        print("API Key: " + str(headers["TRN-Api-Key"]))
        response = requests.get(profile, headers=headers)
        print("TEST " + response.json())
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print("TEST " + soup)
        # kd_element = soup.find('div', class_='kd')
        # if kd_element:
        #     return kd_element.text.strip()
        # else:
        #     raise ValueError("K/D ratio not found in the profile.")
    
    except requests.RequestException as e:
        raise ValueError(f"Error fetching profile data: {e}")
    

if __name__ == "__main__":
    # Example usage
    username = "UhhYeah-"
    profile_url = get_r6siege_profile(username)
    print(f"Profile URL: {profile_url}")
    
    try:
        kd_ratio = get_r6siege_kd(profile_url)
    except ValueError as e:
        print(e)