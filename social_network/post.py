# post.py

from datetime import datetime


class Content:
    
    
    def __init__(self):
        self.author = input("Enter nickname: ")  
        self.text = input("Write your post: ")   
        self.created_at = datetime.now()         

    
    def __str__(self):
        return f"{self.author} said at {self.created_at}: {self.text}"


class Post(Content):

    
    entries = list()

    
    def __init__(self):
        super().__init__()                   
        self.entries.append(self)            
        self.id = len(self.entries)          
        self.likes = 0                       # Initializes the number of likes to 0
        self.dislikes = 0                    # Initializes the number of dislikes to 0

    # Method to increment the number of likes
    def add_like(self):
        self.likes += 1

    # Method to increment the number of dislikes
    def add_dislike(self):
        self.dislikes += 1

    # Method to calculate the rating of the post (likes - dislikes)
    def get_rating(self):
        return self.likes - self.dislikes

    # Class method to sort posts by rating in descending order
    @classmethod
    def sort_by_rating(cls):
        return sorted(cls.entries, key=lambda post: post.get_rating(), reverse=True)

    # String representation of the post object
    def __str__(self):
        return f"#{self.id} {self.author} said: {self.text}\nLikes: {self.likes} Dislikes: {self.dislikes}\nRating: {self.get_rating()}"


class Image:
    pass


class PostWithImage(Post, Image):
    pass


class Comment(Content):

    
    def __init__(self, post_id):
        super().__init__()         
        self.post_id = post_id     

    
    def __str__(self):
        return f"{self.author} commented on {self.post_id}: {self.text}" 


if __name__ == "__main__":

    
    post_with_image = PostWithImage()

    
    comment1 = Comment(1)
    comment2 = Comment(1)

    
    del comment1.author

    
    comment2.note = "some note"

    
    print(comment2)
    print(comment1)
