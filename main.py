import random
import csv

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
	def export_ideas_to_csv(ideas_dict, filename="ideas.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Категория", "Идея"])
        for category, ideas in ideas_dict.items():
            for idea in ideas:
                writer.writerow([category, idea])
    print(f"✓ Идеи экспортированы в {filename}")