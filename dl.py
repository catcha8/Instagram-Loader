import os

os.system("pip install instaloader")

user = input("Username")

os.system(f"instaloader profile {user}")