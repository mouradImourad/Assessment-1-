# Write your video Class here
"""
class Video should include:
* five instance attributes
* videos cls attributes
* four getter 
  _id
  _title
  _rating
  _copies_available
  * one setter for _copies_available getter
* cls method get_a_video_by_title 
* cls method list_inventory
"""

class Video:
    videos = {}
    def __init__(self, _id, _title, _rating, release_year, _copies_available):
        self._id = _id
        self._title = _title
        self._rating = _rating
        self.release_year = release_year
        self._copies_available = _copies_available

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
         if not isinstance(value, int):
              raise ValueError('Copies available shjould be an integer')
         if value < 0:
              raise ValueError('Copies availabe cannot be negative')
         self._copies_available = value
    
    @classmethod
    def get_a_video_by_title(cls, title):
         return cls.videos.get(title, None)
    
    @classmethod
    def add_a_video(cls, video):
         if not isinstance(video, cls):
              raise ValueError("This funciton will only accept an instance of the Video class")
         cls.videos[video.title] = video
    
    @classmethod
    def list_inventory(cls):
         for video in cls.videos.values():
              print(video)
    
    def __str__(self):
         return f"Title: {self.title}, Rating: {self._rating}, Year: {self.release_year}, Available Copies: {self._copies_available}"

