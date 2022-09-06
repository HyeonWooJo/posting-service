import json
import bcrypt

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View
from django.db.models       import Q

from .validation import validate_password
from .models     import Posting


'''
게시물 상세 API
'''
class PostingDetailView(View):
    '''
    # 설명: 게시물 포스팅 API
    # Method: POST
    # uri: /postings/detail
    # Response: 게시물 포스팅 혹은 수정 성공 여부(JSON)
    '''
    def post(self, request):
        try :
            data       = json.loads(request.body)
            title      = data.get('title')
            context    = data.get('context')
            psword     = data.get('psword')
            posting_id = data.get('posting_id')

            validate_password(psword)

            if Posting.objects.filter(id=posting_id).exists():
                Posting.objects.filter(id=posting_id).update(
                    title   = data['title'],
                    context = data['context'],
                )
                return JsonResponse({'message': 'UPDATED'}, status=201)

            hashed_password  = bcrypt.hashpw(psword.encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')

            Posting.objects.create(
                title   = title,
                context = context,
                psword  = decoded_password
            )

            return JsonResponse({'message': 'SUCCESS'}, status = 201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

        except ValidationError as e:
            return JsonResponse({'message': (e.message)}, status = 400)

    '''
    # 설명: 게시물 삭제 API
    # Method: DELETE
    # uri: /postings/detail
    # Response: 게시물 삭제 성공 여부(JSON)
    '''
    def delete(self, request):
        try:
            data        = json.loads(request.body)
            user_psword = data.get('psword')
            posting_id  = data.get('posting_id')
            posting     = Posting.objects.get(id=posting_id)

            encoded_user_psword = user_psword.encode('utf-8')
            encoded_db_psword   = posting.psword.encode('utf-8')

            if not bcrypt.checkpw(encoded_user_psword, encoded_db_psword):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 401)

            posting.delete()

            return JsonResponse({'message': 'DATA_DELETED'}, status=204)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Posting.DoesNotExist:
            return JsonResponse({'message': 'POSTING_DOES_NOT_EXIST'}, status=400)


'''
게시물 리스트 API
'''
class PostingListView(View):
    '''
    # 설명: 게시물 리스트 조회 API
    # Method: GET
    # uri: /postings
    # parameter: offset, limit
    # Response: 게시물 리스트
    '''
    def get(self, request):
        offset = int(request.GET.get('offset', 0))
        limit  = int(request.GET.get('limit', 20))

        q = Q()

        postings = Posting.objects.filter(q).order_by('-created_at')\
                    [offset:offset+limit]

        results = [
            {
                'id': posting.id,
                'title': posting.title,
                'context': posting.context[:10],
            }
            for posting in postings
        ]

        return JsonResponse({'results': results}, status=200)