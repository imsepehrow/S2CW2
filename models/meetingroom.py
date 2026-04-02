from resource import Resource


class MeetingRoom(Resource):

    def __init__(self, resource_id: str, location: str, max_capacity: int,
                 has_projector: bool, seating_layout: str):
        super().__init__(resource_id, location, max_capacity)
        self._has_projector = has_projector
        self._seating_layout = seating_layout

    def get_has_projector(self) -> bool:
        return self._has_projector

    def get_seating_layout(self) -> str:
        return self._seating_layout

    def get_details(self) -> str:
        return (
            f"MeetingRoom ID: {self.get_resource_id()}, "
            f"Location: {self.get_location()}, "
            f"Capacity: {self.get_max_capacity()}, "
            f"Projector: {self._has_projector}, "
            f"Layout: {self._seating_layout}"
        )