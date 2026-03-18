from resource import Resource

class MeetingRoom(Resource):
    def __init__(self, resource_id, location, max_capacity, has_projector, seating_layout):
        super().__init__(resource_id, location, max_capacity)
        self.has_projector = has_projector
        self.seating_layout = seating_layout

    def get_details(self):
        return f"MeetingRoom {self._resource_id}: Projector: {self.has_projector}, Layout: {self.seating_layout}"