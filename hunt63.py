#======================================#
#                                      #
#                                      #
#    Author is not responsible for     #
#       any misuse of the tool.        #
#                                      #
#                                      #
#======================================#

# Type: OSINT
# Author: Semiii
# Contact: r3moved777@protonmail.com
# Github: github.com/semiiixyz
# Language/s: Python3

# Install all required modules
from termcolor import cprint
from bs4 import BeautifulSoup
import sys, requests, time, os


# Interface
def banner():
    cprint('██╗  ██╗██╗   ██╗███╗  ██╗████████╗ █████╗ ██████╗ ', 'blue')
    cprint('██║  ██║██║   ██║████╗ ██║╚══██╔══╝██╔═══╝ ╚════██╗', 'blue')
    cprint('███████║██║   ██║██╔██╗██║   ██║   ██████╗  █████╔╝', 'blue')
    cprint('██╔══██║██║   ██║██║╚████║   ██║   ██╔══██╗ ╚═══██╗', 'red')
    cprint('██║  ██║╚██████╔╝██║ ╚███║   ██║   ╚█████╔╝██████╔╝', 'red')
    cprint('╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝    ╚════╝ ╚═════╝ ', 'red')
    cprint('[     Philippine Phone Number: Reverse Lookup     ]', 'yellow',attrs=['bold'])

def search_yellow_directory(phone_number):
    url = f'https://www.searchyellowdirectory.com/reverse-phone/63{phone_number}/'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and print relevant information
            result_div = soup.find('div', {'class': 'result-data'})
            if result_div:
                result_info = result_div.text.strip()
                print(f'\nResults for {phone_number}:\n{result_info}')
            else:
                print(f'\nNo results found for {phone_number}')
        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    banner()

    # Loading
    print('\nExecuting hunt63.....')
    time.sleep(3)
    os.system('clear')
    banner()

    # Input
    phnumber = input('\nEnter PH number (10 digits): ')
    phnumber = int(phnumber)

    # Perform the search
    search_yellow_directory(phnumber)
