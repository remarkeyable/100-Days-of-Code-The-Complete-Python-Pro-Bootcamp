def get_customer_emails(self):
    customers_endpoint = SHEET_USERS_ENDPOINT
    response = requests.get(customers_endpoint)
    data = response.json()
    self.customer_data = data["users"]
    return self.customer_data