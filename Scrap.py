
# please obey robots.txt


# scraping bot
# type - html or xml
# not JS friendly

# global variable
# default file-name, header-file-name
# file names as tuple
default_file_name = ('data.html')
default_header_file_name = ('header.txt')
default_url = ('https://en.wikipedia.org/wiki/Machine_learning')


# opening file and creating if file is not found
# checks if file can be obtained inside exception function
# if exception is returned, user is asked if file should be created
# in positive response new empty file is created.
# returns last saved data
# parameter - file-name
def open_file(add):

    try:
        file = open(add,'r')

    except IOError:
        print("File not found or path is incorrect")
        print('lets create a file')
        key_stroke = input('Yes/No')
        if (key_stroke.lower() == 'yes'):
            file = open(add,'w+')
            file.write()
            file.close()

    data = file.read()
    if len(data) == 0:
        print('File is empty')

    #else:
    #    print(data)              remove # to print on function call

    file.close()

    return data


# writing file and creating if file is not found
# checks if file can be obtained inside exception function
# if exception is returned, user is asked if file should be created
# in positive response new empty file is created.
# no return
# parameter - file-name, data to write
def write_file(add, write_data):
    try:
        file = open(add, 'w')

    except IOError:

        print("File not found or path is incorrect")
        print('lets create a file')

        key_stroke = input('Yes/No')

        if (key_stroke.lower() == 'yes'):
            file = open(add, 'w+')
            file.write()
            file.close()

    file.writelines(write_data)
    file.close()
    return

# Ask user to give name to file to store or store in default
# returns file-name and url
# parameters - null
def give_name():

    file_name = input('Enter the file-name to dump data \nOr press Enter to save in {}'.format(default_file_name))
    print()
    url = input('Enter the site to scrap \nOr press Enter to scrap {}'.format(default_url))

    if len(file_name) == 0:
        file_name = default_file_name

    if len(url) == 0:
        url = default_url

    return file_name,url


# passes a client Get request
# checks for status code
# initiates write
# returns - null
# parameter - null
def get_method(name):
    import requests

    req = requests.get(name[1], timeout = 1)
    status = req.status_code
    print(status)

    if status == 200:
        da = req.text
        write_file(name[0],da)

    else:
        print('Error, server response code',status, sep = '---')

    req.close()
    return

# beautiful soup
# html parser
# collects all <a> </a> in list
def html_parser(name):
    from bs4 import BeautifulSoup as soup

    with open(name[0]) as fp:
        html_query = soup(fp, 'html.parser')

    html_final = html_query.find_all('a')
    print(html_final[:5])
    return


# main() function
def main():
    name = give_name()
    get_method(name)
    html_parser(name)
    return

main()


