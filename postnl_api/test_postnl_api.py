import argparse
from postnl_api import PostNL_API


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Run the test for PostNL_API")
    parser.add_argument(
        'username', type=str,
        help="Your username (email address)")
    parser.add_argument(
        'password', type=str,
        help="Your password")
    args = parser.parse_args()
    username = args.username
    password = args.password
    # Login using your jouw.postnl.nl credentials
    api = PostNL_API(username, password, 5)

    # Get packages
    print("Get packages")
    packages = api.get_delivery()
    print("Number of packages to be delivered: ", len(packages))
    print("Listing packages:")
    for package in packages:
        print("ID: " + package.id)
        print("Name: " + package.name)
        print("Type: " + package.type)
        print("Status: " + package.status)
        print("Status Message: " + package.status_message)
        print("URL: " + package.url)
        if package.planned_date is not None:
            print("Planned date: " + package.planned_date)
            print("Planned from: " + package.planned_from)
            print("Planned to: " + package.planned_to)
        if package.delivery_date is not None:
            print("Delivery date: " + package.delivery_date)

    packages = api.get_distribution()
    print("Number of packages submitted: ", len(packages))
    print("Listing packages:")
    for package in packages:
        print("ID: " + package.id)
        print("Name: " + package.name)
        print("Type: " + package.type)
        print("Status: " + package.status)
        print("Status Message: " + package.status_message)
        print("URL: " + package.url)
        if package.planned_date is not None:
            print("Planned date: " + package.planned_date)
            print("Planned from: " + package.planned_from)
            print("Planned to: " + package.planned_to)
        if package.delivery_date is not None:
            print("Delivery date: " + package.delivery_date)

    if api.is_letters_activated() is True:
        letters = api.get_letters()
        print("Number of letters: ", len(letters))
        print("Listing letters:")
        for letter in letters:
            print("ID: " + letter.id)
            print("Image URL: " + letter.image)
            print("Status Message: " + letter.status_message)


if __name__ == '__main__':
    main()
