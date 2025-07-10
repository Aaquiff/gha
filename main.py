import os

# Replace 'MY_VAR' with your desired environment variable name
username = os.environ.get('username')
password = os.environ.get('password')

if username is not None:
    print(f"username={username}")
else:
    print(f"username is not set.")

if username is not None:
    print(f"password={password}")
else:
    print(f"password is not set.")
