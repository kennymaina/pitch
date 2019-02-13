import unittest
from app.models import Comment,User,Pitch
from app import db

class CommentModelTest(unittest.TestCase):


    def setUp(self):
            self.user_James = User(username = 'kenneth',password = 'kentoz', email = 'kenny@ms.com')
            self.new_comment = Comment(comment='This movie is the best thing since sliced bread',user = self.user_kenneth,pitch_id=12 )

    def tearDown(self):
            Comment.query.delete()
            User.query.delete()

    def test_check_instance_variable(self):
            self.assertEquals(self.new_comment.comment,Great)
            self.assertEquals(self.new_comment.user,self.user_kenneth)
            self.assertEquals(self.new_comment.pitch_id,12)

    def test_save_comment(self):
            self.new_comment.save_comment()
            self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

            self.new_comment.save_comment()
            got_comments = Comment.get_comments(12)
            self.assertTrue(len(got_comments) == 1)
