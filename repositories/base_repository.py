class BaseRepository:
    
    def __init__(self,  model):
        self.model = model

    def all(self):
        return self.model.all()
    
    def find(self, id):
        return self.model.find(id)

    def delete(self, id):
       return self.model.destroy(id)

    def create(self, data: dict):
      return self.model.create(data)
         

