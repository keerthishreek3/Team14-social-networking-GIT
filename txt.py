import os
import json

PROFILE_FILE = 'user_profiles.json'

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_profiles(profiles):
    with open(PROFILE_FILE, 'w') as f:
        json.dump(profiles, f, indent=4)

def create_profile():
    profiles = load_profiles()
    user_id = input("Enter user ID: ").strip()
    if user_id in profiles:
        print("User already exists.")
        return
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    profiles[user_id] = {'name': name, 'email': email}
    save_profiles(profiles)
    print(f"Profile for {name} created.")

def view_profile():
    profiles = load_profiles()
    user_id = input("Enter user ID to view: ").strip()
    profile = profiles.get(user_id)
    if profile:
        print(f"Name: {profile['name']}\nEmail: {profile['email']}")
    else:
        print("User not found.")

def list_profiles():
    profiles = load_profiles()
    if profiles:
        for user_id, profile in profiles.items():
            print(f"ID: {user_id}, Name: {profile['name']}")
    else:
        print("No profiles found.")

def main():
    while True:
        print("\nUser Profile Directory")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. List Profiles")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            create_profile()
        elif choice == '2':
            view_profile()
        elif choice == '3':
            list_profiles()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import json
import os

PROFILE_FILE = 'user_profiles.json'

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_profiles(profiles):
    with open(PROFILE_FILE, 'w') as f:
        json.dump(profiles, f, indent=4)

def create_profile():
    profiles = load_profiles()
    user_id = input("Enter user ID: ").strip()
    if user_id in profiles:
        print("User already exists.")
        return
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    profiles[user_id] = {'name': name, 'email': email}
    save_profiles(profiles)
    print(f"Profile for {name} created.")

def view_profile():
    profiles = load_profiles()
    user_id = input("Enter user ID to view: ").strip()
    profile = profiles.get(user_id)
    if profile:
        print(f"Name: {profile['name']}\nEmail: {profile['email']}")
    else:
        print("User not found.")

def list_profiles():
    profiles = load_profiles()
    if profiles:
        for user_id, profile in profiles.items():
            print(f"ID: {user_id}, Name: {profile['name']}")
    else:
        print("No profiles found.")

def main():
    while True:
        print("\nUser Profile Directory")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. List Profiles")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            create_profile()
        elif choice == '2':
            view_profile()
        elif choice == '3':
            list_profiles()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import json
import os

PROFILE_FILE = 'user_profiles.json'

def load_profiles():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_profiles(profiles):
    with open(PROFILE_FILE, 'w') as f:
        json.dump(profiles, f, indent=4)

def create_profile():
    profiles = load_profiles()
    user_id = input("Enter user ID: ").strip()
    if user_id in profiles:
        print("User already exists.")
        return
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    profiles[user_id] = {'name': name, 'email': email}
    save_profiles(profiles)
    print(f"Profile for {name} created.")

def view_profile():
    profiles = load_profiles()
    user_id = input("Enter user ID to view: ").strip()
    profile = profiles.get(user_id)
    if profile:
        print(f"Name: {profile['name']}\nEmail: {profile['email']}")
    else:
        print("User not found.")

if __name__ == "__main__":
    while True:
        print("\nUser Profile Directory")
        print("1. Create Profile")
        print("2. View Profile")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            create_profile()
        elif choice == '2':
            view_profile()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

