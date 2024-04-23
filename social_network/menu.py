# menu.py

from post import Post

# Function to add a like to a post
def add_like(post_id):
    # Iterating through all posts in the entries list
    for post in Post.entries:
        # Checking if the current post's ID matches the given post_id
        if post.id == post_id:
            # If found, increment the likes count for the post and print a message
            post.add_like()
            print("Liked!")
            break
    else:
        # If no post with the given ID is found, print a message
        print("Post not found")

# Function to add a dislike to a post
def add_dislike(post_id):
    # Iterating through all posts in the entries list
    for post in Post.entries:
        # Checking if the current post's ID matches the given post_id
        if post.id == post_id:
            # If found, increment the dislikes count for the post and print a message
            post.add_dislike()
            print("Disliked!")
            break
    else:
        # If no post with the given ID is found, print a message
        print("Post not found")

# Function to show posts sorted by rating
def show_posts_sorted_by_rating():
    # Sorting posts by rating (descending order)
    sorted_posts = Post.sort_by_rating()
    # Printing each post in the sorted order
    for post in sorted_posts:
        print(post)


if __name__ == "__main__":
    
    while True:
        print("Welcome to the new social")
        # Menu options
        message = ("""
            Choose the option:
            1. Add post
            2. See all posts
            3. Like a post
            4. Dislike a post
            5. See posts sorted by rating
            0. Exit 

            Your Choice: """)
        
        choice = input(message)
        
        match choice:
            
            case "1":
                new_post = Post()
            
            case "2":
                for entry in Post.entries:
                    print(entry)
            # Case 3: Like a post
            case "3":
                post_id = int(input("Enter the id of the post you want to like: "))
                add_like(post_id)
            # Case 4: Dislike a post
            case "4":
                post_id = int(input("Enter the id of the post you want to dislike: "))
                add_dislike(post_id)
            # Case 5: See posts sorted by rating
            case "5":
                show_posts_sorted_by_rating()
            
            case "0":
                break
            
            case _:
                print("Wrong choice")
