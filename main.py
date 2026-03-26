import random

ideas_by_category = {
    "работа": [
        "Автоматизировать учёт расходов",
        "Создать систему отчётности",
        "Разработать внутренний чат-бот"
    ],
    "хобби": [
        "Написать книгу",
        "Научиться играть на гитаре",
        "Завести блог о путешествиях"
    ],
    "технологии": [
        "Создать мобильное приложение для заметок",
        "Открыть онлайн-курс по программированию",
        "Сделать Telegram-бота для погоды"
    ]
}

def save_to_favorites(idea):
    with open("favorites.txt", "a", encoding="utf-8") as f:
        f.write(idea + "\n")
    print("✓ Идея сохранена в favorites.txt")

def main():
    print("📋 Доступные категории: работа, хобби, технологии")
    category = input("Выберите категорию: ").lower().strip()
    
    if category in ideas_by_category:
        idea = random.choice(ideas_by_category[category])
        print(f"💡 Ваша идея: {idea}")
        
        save = input("Сохранить идею? (да/нет): ").lower().strip()
        if save == "да":
            save_to_favorites(idea)
    else:
        print("❌ Категория не найдена.")

if __name__ == "__main__":
    main()