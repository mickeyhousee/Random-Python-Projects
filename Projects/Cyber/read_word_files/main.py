from docx import Document
import os

def search_word(doc_path, word):
    # Open the Word document using python-docx
    doc = Document(doc_path)

    # Search for the word in paragraphs
    for paragraph in doc.paragraphs:
        if word.lower() in paragraph.text.lower():
            return True

    # Search for the word in table cells
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if word.lower() in cell.text.lower():
                    return True

    return False

def find_and_show_file_paths(word):
    # Walk through the file system starting from the root
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            # Check if the file is a Word document
            if file.endswith(".docx"):
                # Construct the full path of the file
                file_path = os.path.join(root, file)

                # Search for the word in the document
                if search_word(file_path, word):
                    print(root)
                    print(f'The word "{word}" was found in the file:')
                    print(file_path)
                    return True
    return False

word_to_search = 'banana'

if find_and_show_file_paths(word_to_search):
    print(f'The word "{word_to_search}" was found in at least one file.')
else:
    print(f'The word "{word_to_search}" was not found in any files in the file system.')
