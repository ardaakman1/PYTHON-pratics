import sqlite3 as sq

class BudgetManager:
    def __init__(self, db_name="budget.db"):
        self.db_name = db_name
        self.connection = sq.connect(db_name)
        self.cursor = self.connection.cursor()
        print(f"[{db_name}] has connected succesfully!\n\n")

    @property
    def db_name(self):
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        if db_name != "budget.db":
            raise ValueError('\n\nInvalid database\n\n')
        self._db_name = db_name  # setter fonksiyonşar değer döndürmez atama yapar

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):  # burada sadece 3 tane argüman alması gerektiği için rastgele parametreler yolladım
        self._close_connection()
        print("\n\nYOUR DATABASE CLOSED SUCCESFULLY!!\n\n")

    def create_table(self):
        sql_query = """
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        type TEXT
        )
        """  # REAL float gibi ondalıklı sayıları belirtir
        self.cursor.execute(sql_query)
        try:
            self.connection.commit()
            print("\n\nTable checked succesfully!\n\n")
        except:
            print("\n\nTable could not created!\n\n")

    def add_transactions(self, title, amount, type):
        sql_query = """
        INSERT INTO transactions (
        title,
        amount,
        type)
        VALUES (?, ?, ?)
        """
        self.cursor.execute(sql_query, (title, amount, type))
        self.connection.commit()
        print(f"Added: {title} | {amount} | {type.upper()}")

    def show_all_records(self):
        sql_query = "SELECT * FROM transactions"
        self.cursor.execute(sql_query)
        records = self.cursor.fetchall()  # fetchall çekilen sonuçları list of tuples haline getirir
        print("\n\n---ALL RECORDS---\n\n")
        for record in records:
            # record = (1, 'Grocery', 850.5, 'Expense') şeklinde bir tuple (demet) yapısındadır.
            # YAZIM (SYNTAX) DETAYI: :<15 demek "Bu metni sola daya ve yanına 15 karakterlik boşluk bırak" demektir.
            # :>6 ise "Bu sayıyı sağa daya ve 6 karakterlik alan kaplasın" demektir. Sütunların hizalı durmasını sağlar.
            print(f"ID: {record[0]} | Title: {record[1]:<15} | Amount: {record[2]:>6} | Type: {record[3]}\n")
            print("-------------------\n")

    def filtered_results_query(self):
        choice = input("Do you want to see any results filtered by type (y/n)? ")
        choice = choice.upper()
        if choice == 'Y':
            users_choice = input("Please enter the type that you want to search for: ")
            try: 
                self._filtered_results(users_choice)
            except ValueError:
                print(f"Could not found any {users_choice} type\n")

    def _filtered_results(self, type):
        sql_query = """
        SELECT * FROM transactions WHERE type = ?
        """
        self.cursor.execute(sql_query, (type,))  # burda özellikle böyle yazdım type ın tuğle olduğunu belirtmek için
        records = self.cursor.fetchall()
        if not records:
            print(f"\n\nNo records found for your type {type}\n\n")
            return
        print(f"\n\n--- FILTERED RECORDS ({type.upper()}) ---")
        for record in records:
            print(f"ID: {record[0]} | Title: {record[1]:<15} | Amount: {record[2]:>6} | Type: {record[3]}")
        print("-----------------------------------\n")


    def _close_connection(self):
        self.connection.close()
        print("\n\nDatabase connection closed\n\n")

    def control_zone(self):
        choice = input("Dou you want to enter the danger zone? (y/n): ")
        choice = choice.upper()
        if choice == 'Y':
            self._danger_zone()

    def _danger_zone(self):
        print("\n\nENTER 0 TO DELETE THE TABLE")
        print("ENTER 1 TO DELETE Transactions (rows) FROM THE TABLE")
        print("ENTER ELSE FOR EXIT THE DANGER ZONE")
        critic_choice = int(input("PLEASE ENTER YOUR CHOICE: "))

        match critic_choice:
            case 0:
                sql_query = """DELETE FROM transactions"""  # burada DROP TABLE IF EXISTS transactions ta kullanabilirdim ama bilemedim
                self.cursor.execute(sql_query)
                self.connection.commit()  # bir şey ekleme veya silme yaptığımızda o sadece RAM de oluyor bununla SSD den siliyorum
                print("\n\nYOUR DATABASE HAS BEEN DELETED\n\n")
            case 1:
                id_count = int(input("Please enter the number of rows that you are going to delete: "))
                for i in range(id_count):
                    id_to_delete = int(input(f"Please enter the number of the {i + 1} th ID that you want to delete: "))
                    sql_query = """
                    DELETE FROM transactions
                    WHERE id = (?)
                    """
                    try:
                        self.cursor.execute(sql_query, (id_to_delete,))
                        self.connection.commit()  # bir şey ekleme veya silme yaptığımızda o sadece RAM de oluyor bununla SSD den siliyorum
                        print(f"{id_to_delete} has deleted succesfully\n")
                    except sq.Error as error:
                        print(f"An error occured: {error}\n")
                print("\n\nSOME ROWS OF YOUR DATABASE HAS BEEN DELETED\n\n")
            case _:  # default
                pass

        print("\n\nEXITTING THE DANGER ZONE\n\n")

def main():
    with BudgetManager() as budget:
        budget.create_table()
        transaction_number = int(input("Please enter how many transactions that you are going to enter: "))
        for _ in range(transaction_number):
            title = input("Please enter the title of your transaction: ")
            amount = float(input("Please enter amount of your transaction (float): "))
            type = input("Please enter your transaction type: ")
            budget.add_transactions(title, amount, type)

        budget.control_zone()
        budget.filtered_results_query()
        budget.show_all_records()

if __name__ == "__main__":
    main()
   

