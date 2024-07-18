 # GitHub Repositories Privacy Changer

This script is designed to help you change the privacy settings of your public GitHub repositories to private using Python and its libraries `requests` and `BeautifulSoup`. Before running the script, please make sure that you have these libraries installed by running `pip install requests beautifulsoup4`.

## Prerequisites

To use this script, follow these steps:

1. Replace `username` variable with your GitHub username.
2. Set up an empty dictionary named `cookies` under the `s.cookies.update(cookies)` line if needed. Cookies are optional but can improve performance and avoid CAPTCHAs.
3. Update the headers according to your browser configuration.
4. Add any repository names you want to exclude from being made private into the `blacklist` list.
5. Run the script.

## Usage

The script will fetch all the repositories owned by the given user, check their statuses (public or private), and attempt to set those which meet certain conditions (not in the blacklist and not already private) to private. If successful, it will print out the name of the repository and the authentication token used to perform the action.

If there is an error during the process, such as encountering a forked repository or failure to obtain the necessary information, the script will print out the name of the repository along with the error message.

## Limitations

GitHub imposes rate limits on API calls. To prevent hitting these limits, consider adding some delay between each call or breaking down larger lists into smaller chunks. For more details about GitHub's API rate limits, visit https://docs.github.com/en/rest/overview/resources#rate-limiting.