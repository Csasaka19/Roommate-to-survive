import unittest
from models.review import review

class ReviewTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a review instance for testing
        self.review = review(
            room_id="123",
            rating=4.5,
            review_id="456",
            review_text="Example review",
            review_date="2023-07-01",
            user_id="789"
        )

    def test_get_user_id(self):
        # Verify that the correct user ID is returned
        self.assertEqual(self.review.get_user_id(), "789")

    def test_get_room_id(self):
        # Verify that the correct room ID is returned
        self.assertEqual(self.review.get_room_id(), "123")

    def test_get_rating(self):
        # Verify that the correct rating is returned
        self.assertEqual(self.review.get_rating(), 4.5)

    def test_get_review_id(self):
        # Verify that the correct review ID is returned
        self.assertEqual(self.review.get_review_id(), "456")

    def test_get_review_text(self):
        # Verify that the correct review text is returned
        self.assertEqual(self.review.get_review_text(), "Example review")

    def test_get_review_date(self):
        # Verify that the correct review date is returned
        self.assertEqual(self.review.get_review_date(), "2023-07-01")

    def test_set_review(self):
        # Verify that the review attributes are set correctly
        user_id = "987"
        room_id = "654"
        rating = 3.0
        review_id = "321"
        review_text = "New review"
        review_date = "2023-07-02"
        self.review.set_review(user_id, room_id, rating, review_id, review_text, review_date)
        self.assertEqual(self.review.user_id, user_id)
        self.assertEqual(self.review.room_id, room_id)
        self.assertEqual(self.review.rating, rating)
        self.assertEqual(self.review.review_id, review_id)
        self.assertEqual(self.review.review_text, review_text)
        self.assertEqual(self.review.review_date, review_date)

if __name__ == '__main__':
    unittest.main()
