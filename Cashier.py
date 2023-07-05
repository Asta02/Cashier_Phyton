class Transaction:
    count = 0

    """ pembuatan id untuk transaksi yang akan bertambah dari nilai awal count dan di mulai dengan string trs_ """
    def __init__(self):
        Transaction.count += 1
        self.transaction_id = f"trs_{str(Transaction.count).zfill(2)}"
        self.items = []  # Initialize items untuk list kosong

    def add_item(self, item_details):
        """pembuatan item

        Args:
            nama, qty, dan detail
        """
        item_name, item_quantity, item_price = item_details
        item = {
            'name': item_name,
            'quantity': item_quantity,
            'price': item_price
        }
        self.items.append(item)

    def update_item_name(self, item_details):
        """check apakah item_name sama dengan yang di data jika iya nama bisa di update
        """
        item_name, update_name = item_details
        for item in self.items:
            if item['name'] == item_name:
                item['name'] = update_name

    def update_item_qty(self, item_details):
        """check apakah item_name sama dengan yang di data jika iya update qty
        """
        item_name, update_qty = item_details
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] = update_qty

    def update_item_price(self, item_details):
        """check apakah item_name sama dengan yang di data jika iya update price
        """
        item_name, update_price = item_details
        for item in self.items:
            if item['name'] == item_name:
                item['price'] = update_price

    def delete_item(self, item_name):
        self.items = [item for item in self.items if item['name'] != item_name]

    def reset_transaction(self):
        self.items = []

    def check_order(self):
        if self.validate_input():
            self.print_order()
            print("Pemesanan sudah benar")
        else:
            print("Terdapat kesalahan input data")

    def validate_input(self):
        for item in self.items:
            if not all(key in item for key in ['name', 'quantity', 'price']):
                return False
        return True

    def print_order(self):
        print("| No | Nama Item | Jumlah Item | Harga/item | Total Harga |")
        print("|----|-----------|-------------|------------|-------------|")
        for index, item in enumerate(self.items, 1):
            total_price = item['quantity'] * item['price']
            print(f"| {index}  | {item['name']} | {item['quantity']} | {item['price']} | {total_price} |")

    def total_price(self):
        total = sum(item['quantity'] * item['price'] for item in self.items)
        discount = self.calculate_discount(total)
        final_price = total - discount
        return final_price

    def calculate_discount(self, total):
        if total > 500000:
            return total * 0.1  # Diskon 10%
        elif total > 300000:
            return total * 0.08  # Diskon 8%
        elif total > 200000:
            return total * 0.05  # Diskon 5%
        else:
            return 0


# Membuat instance Transaction
trnsct_123 = Transaction()

# Meminta input dari pengguna
print("(ketik 'selesai' untuk mengakhiri)")

while True:
    print("Apa yang ingin Anda lakukan?")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Reset Transaction")
    print("5. Check Order")
    print("6. Total Price")
    print("7. Selesai")

    choice = input("Pilih aksi (1/2/3/4/5/6/7): ")

    if choice == "1":  # Add Item
        item_name = input("Nama Item: ")
        if item_name.lower() == "selesai":
            break
        item_quantity = input("Qty: ")
        if item_quantity.lower() == "selesai":
            break
        item_price = input("Harga: ")
        if item_price.lower() == "selesai":
            break

        try:
            item_quantity = int(item_quantity)
            item_price = int(item_price)
        except ValueError:
            print("Qty dan Harga harus berupa angka. Silakan coba lagi.")
            continue

        trnsct_123.add_item([item_name, item_quantity, item_price])
        print("Item berhasil ditambahkan.")

    elif choice == "2":  # Update Item
        item_name = input("Nama Item yang ingin diupdate: ")
        if item_name.lower() == "selesai":
            break

        print("Apa yang ingin Anda update?")
        print("a. Nama Item")
        print("b. Jumlah Item")
        print("c. Harga Item")

        update_choice = input("Pilih aksi (a/b/c): ")

        if update_choice.lower() == "a":  # Update Nama Item
            new_name = input("Nama Item baru: ")
            trnsct_123.update_item_name([item_name, new_name])
            print("Nama Item berhasil diupdate.")
        elif update_choice.lower() == "b":  # Update Jumlah Item
            new_quantity = int(input("Jumlah Item baru: "))
            trnsct_123.update_item_qty([item_name, new_quantity])
            print("Jumlah Item berhasil diupdate.")
        elif update_choice.lower() == "c":  # Update Harga Item
            new_price = int(input("Harga Item baru: "))
            trnsct_123.update_item_price([item_name, new_price])
            print("Harga Item berhasil diupdate.")
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

    elif choice == "3":  # Delete Item
        item_name = input("Nama Item yang ingin dihapus: ")
        if item_name.lower() == "selesai":
            break
        trnsct_123.delete_item(item_name)
        print("Item berhasil dihapus.")

    elif choice == "4":  # Reset Transaction
        trnsct_123.reset_transaction()
        print("Transaksi berhasil direset.")

    elif choice == "5":  # Check Order
        trnsct_123.check_order()

    elif choice == "6":  # Total Price
        total_price = trnsct_123.total_price()
        discount = trnsct_123.calculate_discount(total_price)
        print("Total belanja: ", total_price)
        print("Diskon: ", discount)

    elif choice == "7":  # Selesai
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
