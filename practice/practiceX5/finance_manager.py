
from decorators import log_transactions

class FinanceManager:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    @log_transactions
    def add_transaction(self, t_type, amount, category):
        if t_type not in ("доход", "расход"):
            print("Ошибка тип должен быть 'доход' или 'расход'.")
        elif amount <= 0:
            print("Ошибка сумма должна быть положительной")
        elif t_type == "расход" and amount > self.balance:
            print("Ошибка недостаточно средств")
        else:
            self.balance += amount if t_type == "доход" else -amount
            self.transactions.append({"type": t_type, "amount": amount, "category": category})
            return True
        return False

    def save_data(self):
        with open("transactions.txt", "w", encoding="utf-8") as f:
            f.write(f"balance:{self.balance}\n")
            for t in self.transactions:
                f.write(f"{t['type']},{t['amount']},{t['category']}\n")

    def load_data(self):
        try:
            with open("transactions.txt", encoding="utf-8") as f:
                lines = f.read().splitlines()
        except FileNotFoundError:
            print("Файл данных не найден Начинаем с пустого баланса")
            return
        self.balance = float(lines[0].split(":")[1])
        for line in lines[1:]:
            t, a, c = line.split(",", 2)
            self.transactions.append({"type": t, "amount": float(a), "category": c})
        print("Данные успешно загружены из файла")

    def run(self):
        while True:
            print("\n1 Добавить доход/расход\n2 Баланс и транзакции\n3 Сохранить и выйти")
            choice = input("Выберите действие : ")
            if choice == "1":
                t_type = input("Введите тип (доход /расход) : ")
                try:
                    amount = float(input("Введите сумму : "))
                except ValueError:
                    print("Ошибка сумма должна быть числом")
                    continue
                self.add_transaction(t_type, amount, input("Введите категорию "))
            elif choice == "2":
                print(f"Текущий баланс : {self.balance}")
                for t in self.transactions:
                    print(t)
            elif choice == "3":
                self.save_data()
                print("Сохранено Программа завершена")
                break
            else:
                print("Ошибка неверная команда")
