import sqlite3 as sq

class BudgetManager:
    def __init__(self, db_name="budget.db"):
        # 1. BAĞLANTI (CONNECTION)
        # SQLite'a bağlanıyoruz. Eğer "budget.db" adında bir dosya yoksa, otomatik olarak yeni yaratır.
        # NASIL ÇALIŞIR?: SQLite bir sunucu (server) değildir. Direkt hard diskindeki bir dosyaya (db_name) okuma/yazma 
        # yetkisiyle bağlanır. Program çalıştığı sürece o dosyayı kilitler (başkası değiştiremesin diye).
        self.connection = sq.connect(db_name)
        # 2. İMLEÇ (CURSOR)
        # İmleç (cursor), bizim veritabanı içinde SQL komutları yazan ve okuyan görünmez elimizdir.
        # NASIL ÇALIŞIR?: Python veritabanına doğrudan komut gönderemez. Cursor objesi, komutları paketleyip 
        # SQLite motoruna ileten ve dönen cevapları (satırları) hafızasında tutup bize sırayla veren bir aracıdır.
        self.cursor = self.connection.cursor()
        print(f"[{db_name}] has connected succesfully!\n\n")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_connection()
        print("\n\nYOUR DATABASE CLOSED SUCCESFULLY!!\n\n")

    def create_table(self):
        # SQL KOMUTU: CREATE TABLE IF NOT EXISTS
        # "transactions" adında bir tablo kur. Eğer zaten varsa hata verme, dokunma.
        # Sütunlar: id (otomatik artan numara), title (metin), amount (sayı), type (metin)
        # NEDEN 3 TIRNAK?: Python'da Enter'a basıp alt satıra geçerek uzun metinler yazmak istiyorsan 
        # """ (üç tırnak) kullanmak zorundasın. Aksi halde Syntax (Yazım) hatası alırsın.
        sql_query = """
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        type TEXT
        )
        """
        # NEDEN AUTOINCREMENT?: id numaralarını biz elle vermeyiz (1, 2, 3 diye). AUTOINCREMENT sayesinde 
        # biz sadece veriyi ekleriz, veritabanı silinenler olsa bile asla çakışmayacak benzersiz bir id atar.
        self.cursor.execute(sql_query)  # Hazırladığımız SQL komutunu elçiye (cursor) verip çalıştırtıyoruz.

        # NEDEN COMMIT?: Veritabanı işlemleri önce RAM'de yapılır. Eğer elektrik kesilirse 
        # tablo silinir. commit() komutu "Yaptığım işlemi RAM'den al, Hard Disk'teki dosyaya kalıcı olarak kazı" demektir.
        try:
            self.connection.commit()
            print("\n\nTable checked/created succesfully\n")
        except:
            print("\n\nTable could not created!\n\n")

    def add_transaction(self, title, amount, transaction_type):
        # SQL KOMUTU: INSERT INTO
        # Tabloya veri ekle. Soru işaretleri (?) güvenlik içindir, verileri oraya daha sonra atarız.
        # NEDEN (?) KULLANIYORUZ?: Eğer f"{title}" şeklinde string formatlama yapsaydık, kötü niyetli biri 
        # title yerine "DROP TABLE transactions" (Tabloyu sil) yazarak (SQL Injection) sistemimizi çökertebilirdi.
        # (?) işareti SQLite'a "Buraya gelecek şeyi sadece DÜZ METİN olarak kabul et, komut olarak algılama" der.
        sql_query = """
        INSERT INTO transactions (
        title,
        amount,
        type)
        VALUES (?, ?, ?)
        """
        self.cursor.execute(sql_query, (title, amount, transaction_type))
        self.connection.commit()
        print(f"Added: {title} | {amount} | {transaction_type}")

    def show_all_records(self):
        # SQL KOMUTU: SELECT
        # * (yıldız) işareti "her şeyi" getir demektir. Tablodaki tüm kayıtları seçiyoruz.
        sql_query = "SELECT * FROM transactions"
        self.cursor.execute(sql_query)

        # fetchall() komutu, seçilen tüm verileri bir liste (list of tuples) olarak getirir.
        # NASIL ÇALIŞIR?: cursor komutu çalıştırdıktan sonra sonuçlar veritabanının bekleme salonundadır. 
        # fetchall() diyerek "Bekleme salonundaki tüm satırları al ve Python'un içine Liste olarak getir" deriz.
        records = self.cursor.fetchall()

        print("\n\n---ALL RECORDS---\n\n")
        for record in records:
            # record = (1, 'Grocery', 850.5, 'Expense') şeklinde bir tuple (demet) yapısındadır.
            # YAZIM (SYNTAX) DETAYI: :<15 demek "Bu metni sola daya ve yanına 15 karakterlik boşluk bırak" demektir.
            # :>6 ise "Bu sayıyı sağa daya ve 6 karakterlik alan kaplasın" demektir. Sütunların hizalı durmasını sağlar.
            print(f"ID: {record[0]} | Title: {record[1]:<15} | Amount: {record[2]:>6} | Type: {record[3]}\n")
            print("-------------------\n")

    def _close_connection(self):
        # İşimiz bittiğinde dosyanın kilitli kalmaması için bağlantıyı kapatıyoruz.
        # NEDEN KAPATIRIZ?: Eğer dosyayı açık unutursak, başka bir Python dosyası veya DB Browser gibi 
        # bir program bu veritabanına bağlanıp işlem yapmak istediğinde "Dosya kilitli (Database is locked)" hatası alır.
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
            transaction_type = input("Please enter your transaction type: ")
            budget.add_transaction(title, amount, transaction_type)

        budget.control_zone()
        budget.show_all_records()

if __name__ == "__main__":
    main()
