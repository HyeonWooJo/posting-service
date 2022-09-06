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