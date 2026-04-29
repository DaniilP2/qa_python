from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert len(collector.get_books_genre()) == 1
        assert 'Гарри Поттер' in collector.get_books_genre()
    
    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0


    def test_set_book_genre_set_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'
        

    def test_get_book_genre_existing_book_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'
        

    def test_get_books_with_specific_genre_multiple_books_returns_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Фантастика')
        collector.set_book_genre('Книга 3', 'Комедии')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 2']
        

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        assert isinstance(collector.get_books_genre(), dict)

    def test_get_books_genre_returns_correct_length_after_adding_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        assert len(collector.get_books_genre()) == 2
        
    def test_get_books_for_children_returns_cartoon_book(self):
        collector = BooksCollector()
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        assert 'Винни Пух' in collector.get_books_for_children()

    def test_get_books_for_children_returns_fantasy_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert 'Гарри Поттер' in collector.get_books_for_children()

    def test_get_books_for_children_does_not_return_horror_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_for_children()
        

    def test_add_book_in_favorites_existing_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()
        

    def test_delete_book_from_favorites_existing_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()
        

    def test_get_list_of_favorites_books_empty_returns_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
        
