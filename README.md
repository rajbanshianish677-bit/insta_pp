Here is your entire project packed beautifully into a single, cohesive `README.md` file that you can drop directly into your GitHub repository. It includes the code, the prerequisites, and the step-by-step setup guide all in one place.

---

### 📄 Paste this entire block into your `README.md`:

```markdown
# Instagram Profile Picture Downloader 📸

A lightweight Python script utilizing `instaloader` to quickly download any Instagram user's profile picture in full resolution. It safely bypasses Instagram's aggressive login walls (`403 Forbidden` errors) by utilizing a local browser cookie session file.

---

## 💻 The Python Code (`insta.py`)

Save the following code inside a file named `insta.py`. It is optimized to clean out clutter and extract only the target profile picture.

```python
import instaloader

# Initialize Instaloader and minimize clutter files
il = instaloader.Instaloader(
    download_geotags=False, 
    download_comments=False, 
    save_metadata=False
)

# 🛠️ EDIT THESE CONFIGURATIONS
your_username = "anish_rajbanshi7"
friend_username = "YOUR_FRIENDS_USERNAME_HERE"  # <-- Put your friend's target handle here

try:
    print("Attempting to load session from cookies.txt...")
    
    # Bypasses the 403 wall completely using the cookie file
    il.load_session_from_file(your_username, filename="cookies.txt")
    
    # Proceed to download the DP
    print(f"\nAttempting to download profile picture for: {friend_username}...")
    il.download_profile(friend_username, profile_pic_only=True)
    
    print("\n" + "="*40)
    print(f"Success! {friend_username}'s DP has been downloaded.")
    print(f"Check the folder named '{friend_username}' in your directory.")
    print("="*40)

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("\nTroubleshooting tips:")
    print("1. Make sure cookies.txt is in the same directory as this script.")
    print("2. Ensure you ran the cookie generation command first (see README).")

```

---

## 🛠️ Prerequisites & Setup

Because Instagram blocks traditional, automated text-logins, you must provide your active browser session cookies to authenticate the script.

### 1. Install Dependencies

Open your terminal and run:

```bash
pip install instaloader browser-cookie3

```

### 2. Export Your Instagram Cookies (One-Time Setup)

1. Open your web browser (Chrome or Firefox) and log into your Instagram account (`anish_rajbanshi7`).
2. Install a lightweight cookie exporter extension (e.g., **Get cookies.txt LOCALLY** for Chrome or **Export Cookies** for Firefox).
3. Navigate to Instagram, click the extension icon, and select **Export**.
4. Save the file as **`cookies.txt`** and move it into the exact same folder where your `insta.py` script lives.

---

## 🚀 Execution

Once your `cookies.txt` file is sitting in your project directory next to `insta.py`, run your script through Python's terminal interface directly:

```powershell
& C:\Python314\python.exe -m instaloader --cookiefile=cookies.txt --no-metadata-json --no-captions anish_rajbanshi7 TARGET_USERNAME

```

*(Make sure to replace `TARGET_USERNAME` with your friend's actual Instagram handle at the end of the command).*

---

## 📁 Output

Upon successful run, a brand-new folder named after your targeted friend will appear in your project workspace containing their clean, high-resolution profile picture (`.jpg`).

---

## 🔒 Security & Constraints

* **Password Safe:** This method never handles your plaintext password, relying exclusively on active browser cookies.
* **Private Accounts:** To download a private account's profile picture, the account associated with your browser cookies (`anish_rajbanshi7`) must already be actively following them.

```

```
