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
    def __init__(self, id, title, rating, release_year, copies_available):
        self._id = id
        self._title = title
        self._rating = rating
        self.release_year = release_year
        self._copies_available = copies_available

    def __repr__(self):
        return f"{self._id} {self._title} {self._rating} {self.release_year} {self._copies_available}"


    @property
    def id(self):
        return self._id
    

    @property
    def title(self):
        return self._title
    

    @property
    def rating(self):
        return self._rating
    

    @property
    def copies_available(self):
        return self._copies_available

    @copies_available.setter
    def copies_available(self, value):
        if not isinstance(value, int):
            raise ValueError('Copies available should be an integer')
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

