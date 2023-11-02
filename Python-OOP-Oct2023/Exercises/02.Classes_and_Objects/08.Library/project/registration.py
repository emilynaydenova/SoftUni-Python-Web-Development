from project.user import User
from project.library import Library
class Registration:
    @staticmethod
    def add_user(user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library):
        if user not in library.user_records:
            return 'We could not find such user to remove!'
        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        found_user = [u for u in library.user_records if u.user_id == user_id]
        if not found_user:
            return f"There is no user with id = {user_id}!"
        lu = found_user[0]
        if lu.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        idx = library.user_records.index(lu)
        library.user_records[idx].username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
