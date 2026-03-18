from resource import (Resource)

class LabSpace(Resource):
    def __init__(self,resource_id,location,max_capacity,number_of_pcs,os_type):
        super().__init__(resource_id,location,max_capacity)
        self.number_of_psc=number_of_pcs
        self.os_type=os_type
    def get_details(self):
        return f"LabSpace {self._resource_id}:{self.number_of_psc}PCs, OS:{self.os_type}"
