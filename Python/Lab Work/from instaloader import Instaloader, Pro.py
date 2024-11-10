from instaloader import Instaloader, Profile

# Create an Instaloader instance
L = Instaloader()

# Login to your Instagram account
L.login("jayesh.p.patel", "jayeshpatel24")

# Specify the target username
target_username = input("Enter User Name : ")

# Download stories from the specified user
profile = Profile.from_username(L.context, target_username)
for story in L.get_stories(userids=[profile.userid]):
    for item in story.get_items():
        L.download_storyitem(item, target_username)