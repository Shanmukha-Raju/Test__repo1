import numpy as np
customer_db = {}
def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter contact number: ")
    cuisine = input("Preferred cuisine (e.g., Indian, Italian, Chinese): ")
    seating = input("Preferred seating (Indoor/Outdoor/Window): ")
    table_numbers = np.arange(1, 21)
    assigned_table = np.random.choice(table_numbers)
    rating = int(input("Initial rating (1–5): "))
    rating_array = np.array([rating])
    bill_payment=int(input("Bill Payment amount: "))
    total_payment=int(input("Total payment amount: "))
    while True:
     if(bill_payment==total_payment):
        print("Transaction is sucessful")
        break
     else:
        print(f"Transaction Amount pending:{(bill_payment)-(total_payment)}")
        options=int(input("enter\n 1 to continue the pending payment \n 2 to pay later:\n "))
        if(options==1):
            pending_amount=int(input("Enter pending amount: "))
            total_payment+=pending_amount
        elif(options==2):
            print("pay amount further ")
            break
     customer_db[contact] = {
        "name": name,
        "cuisine": cuisine,
        "seating": seating,
        "table": assigned_table,
        "rating": rating_array,
        "bill_payment": bill_payment,
        "total_payment": total_payment,
        "pending_amount": (bill_payment)-(total_payment),
    }
    print(f"Customer '{name}' added with Table No: {assigned_table}\n")
def show_customers():
    if not customer_db:
        print("No customers found.\n")
        return
    for contact, details in customer_db.items():
        print(f"Contact: {contact}")
        for key, value in details.items():
            print(f"  {key.capitalize()}: {value}")
        print()
while True:
    print("1. Add Customer")
    print("2. Show Customers")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        add_customer()
    elif choice == '2':
        show_customers()
    elif choice == '3':
        print("Exiting system.")
        break
    else:
        print("Invalid input. Try again.\n")
