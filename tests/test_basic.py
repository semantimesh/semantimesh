def test_import_packages():
    """Проверяет, что все зависимости импортируются без ошибок."""
    try:
        import fastapi
        import uvicorn
        import spacy
        import transformers
        import sklearn
        import redis
        import psycopg2
        print("Все пакеты успешно импортированы!")
    except ImportError as e:
        assert False, f"Ошибка импорта пакета: {e}"
Add basic import test
