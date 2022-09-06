import bcrypt

import json

from django.test import TestCase, Client

from postings.models import Posting


'''
게시물 리스트 API unit test
'''
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

    '''
    게시물 리스트 API success unit test
    '''
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


'''
게시물 상세 API unit test
'''
class PostingDetailView(TestCase):
    def setUp(self):
        Posting.objects.create(
            id      = 1,
            title   = 'I am Saul good man',
            context = 'It is 프리퀄 of Breaking Bad',
            psword  = bcrypt.hashpw('test1234'.encode('utf-8'), 
            bcrypt.gensalt()).decode('utf-8')
        )

    def tearDown(self):
        Posting.objects.all().delete()

    '''
    게시물 리스트 API success unit test
    '''
    def test_success_detail_view_post(self):
        client   = Client()
        body     = {
            'title'   : 'Breaking Bad',
            'context' : 'Best American Drama',
            'psword'  : 'test1234',
        }
        response = client.post(
            "/postings/detail",
            data=json.dumps(body),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'SUCCESS'})

    '''
    게시물 리스트 API success unit test
    '''
    def test_success_detail_view_update(self):
        client   = Client()
        body     = {
            'title'     : 'Breaking Bad',
            'context'   : 'Best American Drama',
            'psword'    : 'test1234',
            'posting_id': 1
        }
        response = client.post(
            "/postings/detail",
            data=json.dumps(body),
            content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'UPDATED'})

    '''
    게시물 리스트 API success unit test
    '''
    def test_success_detail_view_delete(self):
        client   = Client()
        body     = {
            'psword'    : 'test1234',
            'posting_id': 1
        }
        response = client.delete(
            "/postings/detail",
            data=json.dumps(body),
            content_type='application/json')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json(), {'message': 'DATA_DELETED'})