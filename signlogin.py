import streamlit as st
import pyodbc
import re

# Connection string for SQL Server using Windows Authentication
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-SNANA655\MSSQLSERVER01;DATABASE=lipreading;Trusted_Connection=yes;')

new_app_url = "http://localhost:8502/"

def login():
    def validate_email(email):
        # Basic regex pattern for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return False

    # Create a cursor object
    cursor = conn.cursor()


    
    create_table_query = """
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users')
BEGIN
    CREATE TABLE users (
        id INT PRIMARY KEY IDENTITY(1,1),
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL
    )
END
"""

    cursor.execute(create_table_query)
    cursor.commit()

    # Sidebar options
    page = st.sidebar.selectbox("Choose a page", ["Sign Up", "Login","Update Password"])

    # Signup page
    if page == "Sign Up":
        st.title("Sign Up")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Register"):
            if password == confirm_password:
                if validate_email(email):
                    try:
                        # Check if the username already exists
                        select_query = "SELECT * FROM users WHERE username = ?"
                        cursor.execute(select_query, (username,))
                        existing_user = cursor.fetchone()

                        if existing_user:
                            st.error("Username already exists. Please choose a different username.")
                        else:
                            # Insert the new user
                            insert_query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
                            cursor.execute(insert_query, (username, email, password))
                            cursor.commit()
                            st.success("User signed up successfully!")
                    except pyodbc.Error as err:
                        st.error(f"Error: {err}")
                else:
                    st.error("Invalid email format. Please enter a valid email address.")
            else:
                st.error("Passwords do not match. Please try again.")

    # Login page
    elif page == "Login":
        st.title("Log In")
        login_username = st.text_input("Username")
        login_password = st.text_input("Password", type="password")

        if st.button("Log In"):
            select_query = "SELECT * FROM users WHERE username = ? AND password = ?"
            cursor.execute(select_query, (login_username, login_password))
            user = cursor.fetchone()
            if user:
                st.success("Login successful!")
                st.markdown(f'<a href="{new_app_url}" target="_blank">Next</a>', unsafe_allow_html=True)
            else:
                st.error("Invalid username or password.")

    # Update Password page
    elif page == "Update Password":
        st.title("Update Password")
        username = st.text_input("Username")
        new_password = st.text_input("New Password", type="password")
        confirm_new_password = st.text_input("Confirm New Password", type="password")

        if st.button("Update Password"):
            if new_password == confirm_new_password:
                update_query = "UPDATE users SET password = ? WHERE username = ?"
                cursor.execute(update_query, (new_password, username))
                cursor.commit()
                st.success("Password updated successfully!")
            else:
                st.error("New passwords do not match. Please try again.")

    # Close cursor and connection
    cursor.close()

if __name__ == "__main__":
    login()
