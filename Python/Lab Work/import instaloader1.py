import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Define the user profile you want to download
profile = 'vandanaunleashed'

# Download posts and stories
L.download_profile(profile, profile_pic_only=False)
L.download_stories(userids=[profile])

# Alternatively, use an instance of Profile to get stories
profile_instance = instaloader.Profile.from_username(L.context, profile)
for story in L.get_stories(userids=[profile_instance.userid]):
    for item in story.get_items():
        L.download_storyitem(item, target=profile)
