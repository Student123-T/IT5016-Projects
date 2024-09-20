"""
Author:Tanmmey Arora
"""
class Member:
    def __init__(self, student_id, last_name, programme):
        self.student_id = student_id
        self.last_name = last_name
        self.programme = programme
        self.membership_id = None  # Will be assigned by MembershipSystem
class MembershipSystem:
    membership_counter = 1  # Static counter to generate unique membership IDs

    def __init__(self):
        self.registered_members = []
        self.withdrawn_members = []
    def register_member(self, student_id, last_name, programme):
        if programme not in ["Diploma", "Bachelor"]:
            raise ValueError("Invalid programme. Choose 'Diploma' or 'Bachelor'.")
        
        new_member = Member(student_id, last_name, programme)
        new_member.membership_id = MembershipSystem.membership_counter
        MembershipSystem.membership_counter += 1
        
        self.registered_members.append(new_member)
        print(f"Member registered:\nID={new_member.membership_id}\nName={last_name}\nProgramme={programme}")

    def withdraw_member(self, membership_id, last_name):
        for member in self.registered_members:
            if member.membership_id == membership_id and member.last_name == last_name:
                self.registered_members.remove(member)
                print(f"Member withdrawn: ID={membership_id}, Name={last_name}")
                return
        
        print("No matching member found for withdrawal.")

    def display_members(self):
        num_diploma = sum(1 for member in self.registered_members if member.programme == "Diploma")
        num_bachelor = sum(1 for member in self.registered_members if member.programme == "Bachelor")
        
        print("\nCurrent Membership Statistics:")
        print(f"Total Registered Members: {len(self.registered_members)}")
        print(f"Number of Diploma Students: {num_diploma}")
        print(f"Number of Bachelor Students: {num_bachelor}")
        print(f"Number of Withdrawn Members: {len(self.withdrawn_members)}")
        print()

# Example usage
if __name__ == "__main__":
    system = MembershipSystem()
    
    # Registering members
    system.register_member("S1234", "Arora", "Diploma")
    system.register_member("S5678", "Mongia", "Bachelor")
    system.register_member("S5567", "Aman", "Diploma")
    
    # Displaying members
    system.display_members()
    
    # Withdrawing a member
    system.withdraw_member(3, "Aman")
    
    # Displaying members after withdrawal
    system.display_members()
