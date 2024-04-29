from datetime import datetime

class Content:
    
    def __init__(self):
        self.author = input("Enter nickname: ")
        self.text = input("Write your post: ")
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.author} said at {self.created_at}: {self.text}"

class Post(Content):

    entries = []

    def __init__(self):
        super().__init__()
        self.id = len(self.entries) + 1
        self.likes = 0
        self.dislikes = 0

    def __str__(self):
        return (f"#{self.id} {self.author} said: {self.text}. "
            + f"Likes: {self.likes} | Dislikes: {self.dislikes}")

    def __eq__(self, other):
        return self.rating == other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __ge__(self, other):
        return self.rating >= other.rating

    @classmethod
    def show_posts(cls):
        for entry in sorted(cls.entries, reverse=True):
            print(entry)

    def get_rating(self):
        return self.likes - self.dislikes

    @property
    def rating(self):
        return self.get_rating()

    @classmethod
    def find_by_id(cls):
        post_id = input("Enter post id: ")
        for post in cls.entries:
            if post.id == int(post_id):
                return post

    @classmethod
    def like(cls):
        post = cls.find_by_id()
        post.likes += 1

    @classmethod
    def dislike(cls):
        post = cls.find_by_id()
        post.dislikes += 1

    @classmethod
    def save_to_file(cls, filename):
        with open(filename, 'w') as file:
            for post in cls.entries:
                file.write(f"{post.id},{post.author},{post.text},{post.likes},{post.dislikes}\n")

    @classmethod
    def load_from_file(cls, filename):
        cls.entries.clear()
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                post = cls()
                post.id = int(data[0])
                post.author = data[1]
                post.text = data[2]
                post.likes = int(data[3])
                post.dislikes = int(data[4])
                cls.entries.append(post)

class Comment(Content):

    def __init__(self, post_id):
        super().__init__()
        self.post_id = post_id

    def __str__(self):
        return f"{self.author} commented on {self.post_id}: {self.text}" 

if __name__ == "__main__":
    post1 = Post() # rating 0
    post2 = Post() # rating 0
    Post.like()    # Like the first post, rating 1
    Post.save_to_file('posts.txt')
    Post.load_from_file('posts.txt')
    Post.show_posts()
