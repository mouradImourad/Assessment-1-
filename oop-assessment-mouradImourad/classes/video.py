# Write your video Class here
"""
class Video should include:
* five instance attributes
* four getter 
  _id
  _title
  _rating
  _copies_available
  * one setter for _copies_available getter
* cls method get_a_video_by_title 
* cls list_inventory
"""






class Video:

    def __init__(self, id, title, rating, release_year, copies_available):
        self._id = id
        self._title = title
        self._rating = rating
        self.release_year = release_year
        self._copies_available = copies_available

    def __repr__(self):
                return f"{self._id} {self._title} {self._rating} {self.release_year} {self._copies_available}"


    @property
    def get_id(self):
        return self._id
    

    @property
    def get_title(self):
        return self._title
    

    @property
    def get_rating(self):
        return self._rating
    

    @property
    def get_copies_available(self):
        return self._copies_available

    @get_copies_available.setter
    def set_copies_available(self, value):
         pass 
        
    

