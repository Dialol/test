import sys
import warnings
from ebooklib import epub
from bs4 import BeautifulSoup


def parse_epub(file_path):
    # читаем файл
    book = epub.read_epub(file_path)

    # ищем данные в DublinCore 'значение' - стандарт epub
    # получаем кортеж
    # из кортежа вынимаем первое значение
    title = (book.get_metadata('DC', 'title') or [('Неизвестно',)])[0][0]
    author = (book.get_metadata('DC', 'creator') or [('Неизвестно',)])[0][0]
    publisher = (book.get_metadata('DC', 'publisher') or
                 [('Неизвестно',)])[0][0]
    year = (book.get_metadata('DC', 'date') or [('Неизвестно',)])[0][0]

    return title, author, publisher, year


def parse_fb2(file_path):
    # читаем файл
    with open(file_path, 'r', encoding='utf-8') as file:
        book = BeautifulSoup(file, 'xml')

    # получаем данные из xml
        book_title = book.find('book-title')
        book_author = book.find('author')
        book_publisher = book.find('publisher')
        book_year = book.find('date')
    # значение может быть None, поэтому проверка != None
        title = book_title.text if book_title else 'Неизвестно'
    # можно без .split но тогда имя автора будет в столбик
        if book_author:
            author = book_author.text
            author = ' '.join(author.split())
        else:
            author = 'Неизвестно'
        publisher = book_publisher.text if book_publisher else 'Неизвестно'
        year = book_year.text if book_year else 'Неизвестно'

        return title, author, publisher, year


def main():
    # проверяем правильно ли мы запускаем в терминале
    if len(sys.argv) != 2:
        print('Неправильно задан путь к файлу')
        print('python 2.py <file_path>')
        sys.exit(1)

    # считываем значение <file_path>
    file_path = sys.argv[1]

    # в зависимости от файла запускаем функцию
    if file_path.endswith('.epub'):
        result = parse_epub(file_path)
    elif file_path.endswith('.fb2'):
        result = parse_fb2(file_path)
    else:
        print('Не поддерживаемый формат файла')
        sys.exit(1)

    # проверяем полученное значение
    # присваиваем значения кортежа и выводим их
    if result:
        title, author, publisher, year = result
        print(f'Название книги: {title}')
        print(f'Автор: {author}')
        print(f'Издательство: {publisher}')
        print(f'Год: {year}')
    else:
        print('Не удалось извлечь информацию')
        print('Проверьте путь к файлу и его формат')


# функции отрабатывают, но
# отображаются предупреждения, если не найдено одно из значений
warnings.filterwarnings('ignore', category=UserWarning, module='ebooklib')
warnings.filterwarnings('ignore', category=FutureWarning, module='ebooklib')


if __name__ == '__main__':
    main()
