import instaloader

# Initialize Instaloader and minimize clutter files
il = instaloader.Instaloader(
    download_geotags=False, 
    download_comments=False, 
    save_metadata=False
)

your_username = "anish_rajbanshi7"
friend_username = "YOUR_FRIENDS_USERNAME_HERE"  # <-- Change this to your friend's handle

try:
    print("Attempting to load session cookies from your browser...")
    
    # Automatically pulls cookies from Firefox. 
    # (If you use Chrome, change 'firefox' to 'chrome' below)
    il.load_session_from_browser(your_username, browser='firefox')
    
    print("Session successfully loaded! Bypassed Instagram login wall.")
    
    # Proceed to download the DP
    print(f"\nAttempting to download profile picture for: {friend_username}...")
    il.download_profile(friend_username, profile_pic_only=True)
    
    print("\n" + "="*40)
    print(f"Success! {friend_username}'s DP has been downloaded.")
    print(f"Check the folder named '{friend_username}' on your Desktop.")
    print("="*40)

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure you are actively logged into Instagram on your chosen browser.")
    print("2. Close the browser entirely before running the script so Python can access the cookie file.")
    print("3. Change browser='firefox' to browser='chrome' or browser='edge' depending on what you use.")