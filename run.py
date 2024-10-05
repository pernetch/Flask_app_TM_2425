from app import create_app
from app.email.email import send_email

app = create_app()

if __name__ == "__main__":
    
    app.run(debug=True)