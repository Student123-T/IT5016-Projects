"""
Author:Tanmmey Arora
"""
class RequestSystem:
    # Class-level attribute for unique ID counter
    _id_counter = 1

    def __init__(self):
        # Instance-level attributes
        self.requests = []
    
    def user_info(self, name, age, email):
        """Collects user details and returns a unique ID for the request."""
        user_id = RequestSystem._id_counter
        RequestSystem._id_counter += 1
        return {
            'user_id': user_id,
            'name': name,
            'age': age,
            'email': email
        }

    def request_details(self, items):
        """Accepts a list of request items with their costs and calculates the total."""
        total_amount = sum(cost for item, cost in items)
        return {
            'items': items,
            'total_amount': total_amount
        }

    def request_approval(self, total_amount):
        """Decides if the request is approved based on the total amount."""
        return "approved" if total_amount < 150 else "pending"

    def respond_request(self, request_id, status):
        """Allows a manager to respond to a pending request, marking it as Approved or Not Approved."""
        for req in self.requests:
            if req['user_id'] == request_id:
                if req['status'] == "pending":
                    req['status'] = status
                else:
                    print(f"Request {request_id} is already {req['status']}.")
                break
        else:
            print(f"Request {request_id} not found.")

    def display_request(self):
        """Prints information for all request objects."""
        for req in self.requests:
            print(f"Request ID: {req['user_id']}, Name: {req['name']}, Total: ${req['total_amount']}, Status: {req['status']}")

    def request_statistic(self):
        """Displays statistical information about the requisitions."""
        total_requests = len(self.requests)
        approved_requests = sum(1 for req in self.requests if req['status'] == 'approved')
        pending_requests = sum(1 for req in self.requests if req['status'] == 'pending')
        not_approved_requests = sum(1 for req in self.requests if req['status'] == 'not approved')

        print(f"Total Requests: {total_requests}")
        print(f"Total Approved Requests: {approved_requests}")
        print(f"Total Pending Requests: {pending_requests}")
        print(f"Total Not Approved Requests: {not_approved_requests}")

    def create_request(self, name, age, email, items):
        """Combines user info, request details, and approval into one request."""
        user = self.user_info(name, age, email)
        details = self.request_details(items)
        status = self.request_approval(details['total_amount'])
        
        request = {
            'user_id': user['user_id'],
            'name': user['name'],
            'age': user['age'],
            'email': user['email'],
            'items': details['items'],
            'total_amount': details['total_amount'],
            'status': status
        }
        
        self.requests.append(request)

# Example usage:
if __name__ == "__main__":
    rs = RequestSystem()

    # Creating some requests
    rs.create_request("Tanmmey Arora", 30, "tanny@example.com", [("Item A", 50), ("Item B", 60)])
    rs.create_request("Aman Prajapati", 45, "Aman@example.com", [("Item C", 120)])

    # Display all requests
    rs.display_request()

    # Display statistics
    rs.request_statistic()

    # Respond to a request
    rs.respond_request(1, "not approved")

    # Display all requests after response
    rs.display_request()
    
    # Display statistics after response
    rs.request_statistic()
    