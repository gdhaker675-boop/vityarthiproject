complaints = []
complaint_id = 1
def register_complaint():
    global complaint_id

    print("\n--- Register Complaint ---")

    name = input("Enter Student Name: ")
    room = input("Enter Room Number: ")

    print("\nSelect Complaint Category:")
    print("1. Hostel")
    print("2. Mess")

    category_choice = input("Enter your choice: ")

    if category_choice == "1":
        category = "Hostel"
    elif category_choice == "2":
        category = "Mess"
    else:
        print("Invalid category!")
        return

    complaint = input("Enter Complaint Description: ")

    data = {
        "ID": complaint_id,
        "Name": name,
        "Room": room,
        "Category": category,
        "Complaint": complaint,
        "Status": "Pending"
    }

    complaints.append(data)

    print("\nComplaint Registered Successfully!")
    print("Your Complaint ID is:", complaint_id)

    complaint_id += 1
def view_complaints():
    print("\n--- All Complaints ---")

    if not complaints:
        print("No complaints found.")
        return

    for c in complaints:
        print("\nComplaint ID:", c["ID"])
        print("Student Name:", c["Name"])
        print("Room Number:", c["Room"])
        print("Category:", c["Category"])
        print("Complaint:", c["Complaint"])
        print("Status:", c["Status"])
def check_status():
    print("\n--- Check Complaint Status ---")

    cid = input("Enter Complaint ID: ")

    for c in complaints:
        if str(c["ID"]) == cid:
            print("\nComplaint ID:", c["ID"])
            print("Student Name:", c["Name"])
            print("Complaint:", c["Complaint"])
            print("Status:", c["Status"])
            return

    print("Complaint ID not found.")
def update_status():
    print("\n--- Update Complaint Status ---")

    cid = input("Enter Complaint ID: ")

    for c in complaints:
        if str(c["ID"]) == cid:

            print("\n1. Pending")
            print("2. In Progress")
            print("3. Resolved")

            choice = input("Select New Status: ")

            if choice == "1":
                c["Status"] = "Pending"
            elif choice == "2":
                c["Status"] = "In Progress"
            elif choice == "3":
                c["Status"] = "Resolved"
            else:
                print("Invalid choice!")
                return

            print("Complaint Status Updated Successfully!")
            return

    print("Complaint ID not found.")

while True:

    print("\n================================")
    print(" HOSTEL/MESS COMPLAINT SYSTEM")
    print("================================")

    print("1. Register Complaint")
    print("2. View All Complaints")
    print("3. Check Complaint Status")
    print("4. Update Complaint Status (Admin)")
    print("5. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        register_complaint()

    elif choice == "2":
        view_complaints()

    elif choice == "3":
        check_status()

    elif choice == "4":
        update_status()

    elif choice == "5":
        print("\nThank you for using the system!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
