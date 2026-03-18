class Resource:
    def __init__(self,resource_id,location,max_capacity):
        self._resource_id=resource_id
        self._location=location
        self._max_capacity=max_capacity
    def get_recource_id(self):
        return self._resource_id
    def get_location(self):
        return self._location
    def get_max_capacity(self):
        return self._max_capacity
    def get_details(self):
     return f"Resource{self._resource_id} at {self._location} , Capacity : {self._max_capacity}"