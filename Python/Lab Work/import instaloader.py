import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Define the user profile you want to download
profile = 'chunara3496'

# Download profile
L.download_profile(profile, profile_pic_only=False)
