"""
Скрипт для запуска веб-интерфейса
"""
from website.app import app

if __name__ == "__main__":
    app.run(debug=True) 