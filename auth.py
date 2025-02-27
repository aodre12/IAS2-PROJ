import time
from database import get_user, update_user

def login(username, password):
    current_time = time.time()
    
    user = get_user(username)
    
    if not user:
        return "❌ User not found!"

    user_id, db_username, db_password, failed_attempts, locked_until = user

    # Check if account is locked
    if locked_until > current_time:
        return "🔒 Account is locked! Try again later."

    # Validate password
    if password == db_password:
        update_user(username, 0, 0)  # Reset failed attempts
        return "✅ Login successful!"
    else:
        failed_attempts += 1

        # Lock account after 5 failed attempts
        if failed_attempts >= 5:
            lock_time = current_time + 300  # Lock for 5 minutes
            update_user(username, failed_attempts, lock_time)
            return "🚨 Too many failed attempts! Account locked for 5 minutes."
        
        update_user(username, failed_attempts, locked_until)
        return "❌ Invalid password!"
