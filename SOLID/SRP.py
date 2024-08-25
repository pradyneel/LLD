# Example for Single Responsibilty Priciple

class UserAuthenticator:
    def authenticate_user(self, username, password):
        # Authentication logic
        pass

class UserProfileManager:
    def update_usre_profile(self, user_id, new_profile_data):
        # Profile update logic
        pass

class EmailNotifier:
    def send_email_notification(self, user_email, message):
        # Email sending logic
        pass