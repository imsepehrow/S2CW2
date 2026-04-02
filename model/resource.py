class Resource:
    # Base class for all of them
    def __init__(self, resource_id: str, location: str, max_capacity: int):
        # private attributes
        self._resource_id = resource_id
        self._location = location
        self._max_capacity = max_capacity

    def get_resource_id(self) -> str:
        return self._resource_id
    # getter for resource id

    def get_location(self) -> str:
        return self._location
    # getter for location

    def get_max_capacity(self) -> int:
        return self._max_capacity
# getter for capacity
    def get_details(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")
    # this method must be overridden in subclasses
