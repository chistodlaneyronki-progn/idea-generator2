import random

ideas = [
    "Написать книгу",
    "Создать мобильное приложение для заметок",
    "Открыть онлайн-курс по программированию",
    "Автоматизировать учёт расходов",
    "Сделать Telegram-бота для погоды",
    "Изучить Git"  # Добавили новую идею
]

def save_to_favorites(idea):
    with open("favorites.txt", "a", encoding="utf-8") as f:
        f.write(idea + "\n")
    print("Идея сохранена в favorites.txt")

def main():
    idea = random.choice(ideas)
    print(f"Ваша идея: {idea}")
    
    save = input("Сохранить идею? (да/нет): ").lower().strip()
    if save == "да":
        save_to_favorites(idea)

if __name__ == "__main__":
    main()