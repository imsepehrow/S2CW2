class Booking:

    def __init__(self, booking_id: str, resource, user, date: str,
                 time_slot: str, attendees: int):
        self._booking_id = booking_id
        self._resource = resource
        self._user = user
        self._date = date
        self._time_slot = time_slot
        self._attendees = attendees

    def get_booking_id(self) -> str:
        return self._booking_id

    def get_resource(self) -> "Resource":
        return self._resource

    def get_user(self) -> "User":
        return self._user

    def get_date(self) -> str:
        return self._date

    def get_time_slot(self) -> str:
        return self._time_slot

    def get_attendees(self) -> int:
        return self._attendees
# display full booking information
    def get_booking_details(self) -> str:
        return (
            f"Booking ID: {self._booking_id}, "
            f"User: {self._user.get_name()}, "
            f"Resource: {self._resource.get_details()}, "
            f"Date: {self._date}, "
            f"Time Slot: {self._time_slot}, "
            f"Attendees: {self._attendees}"
        )
