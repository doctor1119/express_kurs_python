# Описание задачи

Разработать асинхронный парсер статей с сайта habr.com, который извлекает следующую информацию о каждой статье: название, автора, дату и время публикации, краткое содержание и ссылку на полный текст статьи.

# Детализированные требования

- **Входные данные**: Парсер должен принимать HTTP GET запрос, содержащий параметр `page_count`, который определяет количество страниц для парсинга.
- **Асинхронность**: Реализация парсера должна использовать асинхронные операции для улучшения производительности и обеспечения неблокирующего ввода/вывода.
- **Структура ответа**: Ответ должен быть в формате JSON, где каждая статья представлена объектом с ключами: "title", "author", "url", "date", "summary". Массив таких объектов группируется по страницам, на которых были найдены статьи.
- **Обработка ошибок**: Парсер должен корректно обрабатывать возможные ошибки во время HTTP запросов и парсинга HTML, возвращая клиенту соответствующие HTTP статусы и сообщения об ошибках.
- **Логирование**: Должно быть реализовано логирование ключевых событий в процессе работы парсера для упрощения отладки и мониторинга.
- **Оптимизация**: Парсер должен быть оптимизирован для работы с большими объемами данных с минимальным временем отклика.

# Пример структуры ответа

```json
{
  "page_data": [
    {
      "title": "Заголовок статьи",
      "author": "Имя автора",
      "url": "https://habr.com/ru/post/123456/",
      "date": "2023-01-01T12:00:00",
      "summary": "Краткое содержание статьи..."
    },
    ...
  ],
  ...
}
```

# Документация и инструменты

- FastAPI для создания асинхронного веб-сервиса: https://fastapi.tiangolo.com/ru/
- Beautiful Soup для парсинга HTML-страниц: https://beautiful-soup.readthedocs.io/en/latest/
- Aiohttp для асинхронного выполнения HTTP запросов: https://docs.aiohttp.org/en/stable/

# Дополнительные указания

- Предусмотреть возможность расширения функциональности парсера, например, добавление дополнительных полей в результат или изменение источника данных.