class Booking:
    def __init__(self, booking_id, resource, user, date, time_slot, attendees):
        self.booking_id = booking_id
        self.resource = resource
        self.user = user
        self.date = date
        self.time_slot = time_slot
        self.attendees = attendees

    def get_booking_details(self):
        return f"Booking {self.booking_id} by {self.user.get_name()} for {self.resource.get_details()} on {self.date} at {self.time_slot}"