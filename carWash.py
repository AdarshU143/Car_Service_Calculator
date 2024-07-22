def main():
    service_cost = {
        'Air freshener': 1,
        'Rain repellent': 2,
        'Tire shine': 2,
        'Wax': 3,
        'Vacuum': 5
    }

    base = 10
    total = base
    selected_services = []

    print("Base wash - $10")

    while True:
        service = input("Enter additional service (or 'done' to finish): ").capitalize()

        if service == 'Done':
            break

        try:
            cost = service_cost[service]
            total += cost
            selected_services.append((service, cost))
        except KeyError:
            print("Sorry, that service is not available. Please try again.")

    for service, cost in selected_services:
        print(f"{service} - ${cost}")

    print("----------")
    print("Total price - $" + str(total))

if __name__ == "__main__":
    main()
