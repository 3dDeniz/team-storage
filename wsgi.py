import sys
sys.path.append('/home/3dDeniz/team-storage')  # Adjust to your project directory

from main import app as application  # Ensure this matches your Flask app instance

if __name__ == "__main__":
    application.run()
