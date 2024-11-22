def login(user, password):
    if not user or not password:
        print("Error: Missing credentials!")
        return
    print(f"Logging in {user}...")
