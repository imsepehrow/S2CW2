from resource import Resource

# labspace inherits from resource
class LabSpace(Resource):
    def __init__(self, resource_id: str, location: str, max_capacity: int,
                 number_of_pcs: int, os_type: str):
        # call parent constructor
        super().__init__(resource_id, location, max_capacity)
        # private attributes specific to LabSpace
        self._number_of_pcs = number_of_pcs
        self._os_type = os_type

    def get_number_of_pcs(self) -> int:
        return self._number_of_pcs

    def get_os_type(self) -> str:
        return self._os_type

    def get_details(self) -> str:
        return (
            f"LabSpace ID: {self.get_resource_id()}, "
            f"Location: {self.get_location()}, "
            f"Capacity: {self.get_max_capacity()}, "
            f"PCs: {self._number_of_pcs}, "
            f"OS: {self._os_type}"
        )
