import \
    xml.etree.ElementTree as ET  # ElementTree is a class that wraps the element structure and allows conversion to and
# from XML.
import openpyxl as wb  # is a Python library to read/write Excel


def main():
    # parse the XML file
    my_tree = ET.parse('compiler.xml')

    # get the root element
    root = my_tree.getroot()
    # create a new Excel file and add an empty sheet
    workbook = wb.Workbook()
    sheet = workbook.active
    # add the headings in the empty Excel sheet
    sheet.append(['Book ID', 'Author Name', 'Title', 'Genre', 'Price', 'Publish Date', 'Description'])
    # extract the data and add it to the Excel sheet
    for book in root:
        book_id = book.get('id')
        author_name = book.find('author').text
        title = book.find('title').text
        genre = book.find('genre').text
        price = book.find('price').text
        publish_date = book.find('publish_date').text
        description = book.find('description').text
        sheet.append([book_id, author_name, title, genre, price, publish_date, description])
        # print the extracted data
        print(f'Book ID: {book_id}')
        print(f'Author Name: {author_name}')
        print(f'Title: {title}')
        print(f'Genre: {genre}')
        print(f'Price: {price}')
        print(f'Publish Date: {publish_date}')
        print(f'Description: {description}')
        print("\n")

    # save the Excel sheet
    workbook.save('200901104_Assign_03.xlsx')
    workbook.close()
    print("The data has been successfully extracted from given XML file and saved in excel sheet")


if __name__ == '__main__':
    main()
