from email.quoprimime import body_check
import json

from django.test import TestCase, Client

from postings.models import Posting


class PostingListView(TestCase):
    def setUp(self):
        Posting.objects.create(
            id      = 1,
            title   = 'I am Saul good man',
            context = 'It is 프리퀄 of Breaking Bad',
            psword  = '1asdfg'
        )

    def tearDown(self):
        Posting.objects.all().delete()

    # 자유게시판 리스트 조회 API unit test
    def test_success_list_view_get(self):
        client   = Client()
        response = client.get(
            "/postings?offset=0&limit=1", 
            content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'results' : [{
            'id'      : 1,
            'title'   : 'I am Saul good man',
            'context' : 'It is 프리퀄 '
        }]})


class PostingDetailView(TestCase):
    def setUp(self):
        Posting.objects.create(
            id      = 1,
            title   = 'I am Saul good man',
            context = 'It is 프리퀄 of Breaking Bad',
            psword  = '1asdfg'
        )

    def tearDown(self):
        Posting.objects.all().delete()

    def test_success_detail_view_post(self):
        client   = Client()
        body     = {
            'title'   : 'Breaking Bad',
            'context' : 'Best American Drama',
            'psword'  : '2asdfg',
        }
        response = client.post(
            "/postings/detail",
            data=json.dumps(body),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'SUCCESS'})

    def test_success_detail_view_update(self):
        client   = Client()
        body     = {
            'title'   : 'Breaking Bad',
            'context' : 'Best American Drama',
            'psword'  : '1asdfg',
            'posting_id': 1
        }
        response = client.post(
            "/postings/detail",
            data=json.dumps(body),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'UPDATED'})