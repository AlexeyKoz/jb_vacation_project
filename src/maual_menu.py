def run_manual_menu(user_service, role_service, country_service, vacation_service, like_service):
    """Manual testing menu."""
    while True:
        print("\nChoose an option:")

        # User-related operations
        print("1  - Create a new user (non-admin)")
        print("2  - Get all users")
        print("3  - Check if email exists")
        print("4  - Return user by email and password")
        print("5  - Delete a user")
        print("6  - Get user by ID")
        print("7  - Update user role")
        print("8  - Login")
        print("")

        # Role-related operations
        print("9  - Create a new role")
        print("10 - Get all roles")
        print("11 - Get role by ID")
        print("")

        # Country-related operations
        print("12 - Create a new country")
        print("13 - Get all countries")
        print("14 - Get country by ID")
        print("15 - Update country by ID")
        print("16 - Delete a country")
        print("")

        # Like-related operations
        print("17 - Like a vacation")
        print("18 - Unlike")
        print("19 - Get likes by user")
        print("20 - Get all Likes")
        print("")

        # Vacation-related operations
        print("21 - Create a new vacation")
        print("22 - Get all vacations")
        print("23 - Get vacation by ID")
        print("24 - Update vacation")
        print("25 - Delete vacation")

        # Exit
        print("26 - Exit")

        choice = input("Enter option: ")

        # User-related actions
        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            password = input("Password: ")

            print("Available roles:")
            roles = role_service.get_all_roles()
            for role in roles:
                print(f"{role.id} - {role.name}")

            role_id = int(input("Enter Role ID: "))
            if role_id == 1:
                print("Error: Cannot create another administrator!")
            else:
                user = user_service.create_user(first_name, last_name, email, password, role_id)
                print("User created:", user.as_dict() if user else "Error")

        elif choice == "2":
            users = user_service.get_all_users()
            print("Users:", [user.as_dict() for user in users])

        elif choice == "3":
            email = input("Enter email to check: ")
            exists = user_service.check_email_exists(email)
            print("This email is", "already registered." if exists else "available.")

        elif choice == "4":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = user_service.get_user_by_email_and_password(email, password)
            print("User found:", user.as_dict() if user else "Error: User not found.")

        elif choice == "5":
            user_service.delete_user_by_input()

        elif choice == "6":
            user_id = int(input("User ID: "))
            user = user_service.get_user_by_id(user_id)
            print("User found:", user.as_dict() if user else "Error")

        elif choice == "7":
            user_id = int(input("Enter User ID: "))
            print("Available roles:")
            roles = role_service.get_all_roles()
            for role in roles:
                print(f"{role.id} - {role.name}")

            new_role_id = int(input("Enter new Role ID: "))
            updated_user = user_service.update_user_role(user_id, new_role_id)
            print("User role updated:", updated_user.as_dict() if updated_user else "Error updating user role")

        elif choice == "8":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = user_service.login(email, password)
            print("User logged in." if user else "Login failed.")

        # Role-related actions
        elif choice == "9":
            role_name = input("Enter new role name: ")
            if role_name.lower() == "admin":
                print("Error: Cannot create another administrator role!")
            else:
                role = role_service.create_role(role_name)
                print("Role created:", role.as_dict() if role else "Error")

        elif choice == "10":
            roles = role_service.get_all_roles()
            print("Roles:", [role.as_dict() for role in roles])

        elif choice == "11":
            role_id = int(input("Role ID: "))
            role = role_service.get_role_by_id(role_id)
            print("Role found:", role.as_dict() if role else "Error")

        # Country-related actions
        elif choice == "12":
            country_name = input("Country name: ")
            country = country_service.create_country(country_name)
            print("Country created:", country.as_dict() if country else "Error")

        elif choice == "13":
            countries = country_service.get_all_countries()
            print("Countries:", [country.as_dict() for country in countries])

        elif choice == "14":
            country_id = int(input("Country ID: "))
            country = country_service.get_country_by_id(country_id)
            print("Country found:", country.as_dict() if country else "Error")

        elif choice == "15":
            country_id = int(input("Enter country ID to update: "))
            country_name = input("New country name: ")
            country = country_service.update_country(country_id, country_name)
            print("Country updated:", country.as_dict() if country else "Error updating country.")

        elif choice == "16":
            country_id = int(input("Enter Country ID to delete: "))
            deleted = country_service.delete_country(country_id)
            print("Country deleted." if deleted else "Error deleting country.")

        # Like-related actions
        elif choice == "17":
            user_id = int(input("User ID: "))
            vacation_id = int(input("Vacation ID: "))
            like = like_service.add_like(user_id, vacation_id)
            print("Vacation liked." if like else "Error liking vacation.")

        elif choice == "18":
            user_id = int(input("User ID: "))
            vacation_id = int(input("Vacation ID: "))
            removed = like_service.remove_like(user_id, vacation_id)
            print("Like removed." if removed else "Error removing like.")

        elif choice == "19":
            user_id = int(input("User ID: "))
            likes = like_service.get_likes_by_user(user_id)
            print("User's likes:", [like.as_dict() for like in likes])

        elif choice == "20":
            likes = like_service.get_all_likes()
            print("Likes:", [like.as_dict() for like in likes])

        # Vacation-related actions (fully restored)
        elif choice == "21":
            country_id = int(input("Country ID: "))
            description = input("Description: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            price = float(input("Price: "))
            image_url = input("Image URL: ")

            vacation = vacation_service.create_vacation(country_id, description, start_date, end_date, price, image_url)
            print("Vacation created:", vacation.as_dict() if vacation else "Error")

        elif choice == "22":
            vacations = vacation_service.get_all_vacations()
            print("Vacations:", [vac.as_dict() for vac in vacations])

        elif choice == "23":
            vacation_id = int(input("Vacation ID: "))
            vacation = vacation_service.get_vacation_by_id(vacation_id)
            print("Vacation found:", vacation.as_dict() if vacation else "Error")

        elif choice == "24":
            vacation_id = int(input("Enter vacation ID to update: "))
            country_id = int(input("Country ID: "))
            description = input("Description: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            price = float(input("Price: "))
            image_url = input("Image URL: ")

            vacation = vacation_service.update_vacation(vacation_id, country_id, description, start_date, end_date, price, image_url)
            print("Vacation updated:", vacation.as_dict() if vacation else "Error updating vacation.")

        elif choice == "25":
            vacation_id = int(input("Enter Vacation ID to delete: "))
            deleted = vacation_service.delete_vacation(vacation_id)
            print("Vacation deleted." if deleted else "Error: Vacation not found or could not be deleted")

        elif choice == "26":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")
