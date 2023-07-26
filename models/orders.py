class Order():
    """Class that defines the properties for an order object"""
    def __init__(self, id, metalId, styleId, sizeId):
        self.id = id
        self.metalId = metalId
        self.styleId = styleId
        self.sizeId = sizeId
        self.metal = None
        self.style = None
        self.size = None