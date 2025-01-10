# config.py

class Config:
    # MySQL database URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Kathir%409360%40@localhost:3306/procore_db'
    
    # Secret key for session management and security
    SECRET_KEY = '2f1a3c4e5f6a7b8c9d0e1f2a3b4c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9r0s1t2'  # Update with your own secret key
    
    # Disable modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
