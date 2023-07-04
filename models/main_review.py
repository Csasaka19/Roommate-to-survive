#!/usr/bin/python3
"""This is the main review module.It creates a review instance and prints the review attributes"""
from models.review import review

def main():
    # Create a review instance
    user_id = 123
    room_id = 1
    rating = 4.5
    review_id = 1
    review_text = "Great experience! Highly recommended."
    review_date = "2023-07-03"
    my_review = review(user_id, room_id, rating, review_id, review_text, review_date)

    # Get and print review attributes
    print("User ID:", my_review.get_user_id())
    print("Room ID:", my_review.get_room_id())
    print("Rating:", my_review.get_rating())
    print("Review ID:", my_review.get_review_id())
    print("Review Text:", my_review.get_review_text())
    print("Review Date:", my_review.get_review_date())

    # Set new review attributes
    new_user_id = 456
    new_room_id = 2
    new_rating = 3.8
    new_review_id = 2
    new_review_text = "Average stay. Room could be cleaner."
    new_review_date = "2023-07-04"
    my_review.set_review(new_user_id, new_room_id, new_rating, new_review_id, new_review_text, new_review_date)

    # Get and print updated review attributes
    print("Updated User ID:", my_review.get_user_id())
    print("Updated Room ID:", my_review.get_room_id())
    print("Updated Rating:", my_review.get_rating())
    print("Updated Review ID:", my_review.get_review_id())
    print("Updated Review Text:", my_review.get_review_text())
    print("Updated Review Date:", my_review.get_review_date())

if __name__ == "__main__":
    main()
