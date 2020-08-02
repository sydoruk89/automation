import re, logging
try:
    def read_file(path):
        """ The function takes data from text file and return a stripped string.
        Args:
            path (txt): txt file
        """
        with open(path, 'r') as words_read:
            text = words_read.read()
            return text
except FileNotFoundError as error:
    print(error)

stored_text = read_file('assets/potential-contacts.txt')

try:
    def find_phone_numbers(data):
        """
        This function returns a list with phone numbers.

        Args:
            data ([str])
        """
        numbers_list = []
        pattern = r'[0-9]\d+-\d+-\d+|\d{9,10}|\d+\.\d+\.\d+|\(\d+\)\d+\-\d+'
        numbers = re.findall(pattern, data)
        for el in sorted(numbers):
            new_el = re.sub('\.|\(|\)|\-', '', el)
            formatted_number = '-'.join([new_el[:3], new_el[3:6], new_el[6:]]) + ' \n'
            if formatted_number not in numbers_list:
                numbers_list.append(formatted_number)
        return numbers_list
except Exception as ex:
    logging.exception(ex)

try:
    def print_numbers():
        """
        This function return a str with phone numbers.

        Args:
            data ([str])
        """
        numbers_str = ''
        sorted_numbers = sorted(find_phone_numbers(stored_text))
        for el in sorted_numbers:
            numbers_str += el
        return numbers_str
except Exception as ex:
    logging.exception(ex)

try:
    def print_email(data):
        """
        This function returns a str with email numbers.

        Args:
            data ([str])
        """
        email_text = ''
        pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        email = re.findall(pattern, data)
        for el in sorted(email):
            email_text += f'{el}\n'
        return email_text
except Exception as ex:
    logging.exception(ex)
        

try:
    def write_numbers(name):
        """Write down a new file with phone numbers.
        """
        with open(name, 'w+') as write_file:
            result = write_file.write(print_numbers())
            return result
except Exception as ex:
    logging.exception(ex)

try:
    def write_email(name):
        """Write down a new file with emails.
        """
        with open(name, 'w+') as write_file:
            result = write_file.write(print_email(stored_text))
            return result
except Exception as ex:
    logging.exception(ex)

if __name__ == "__main__":
    write_numbers('assets/phone_numbers.txt')
    write_email('assets/emails.txt')
