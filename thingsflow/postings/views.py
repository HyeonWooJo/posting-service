import json
import bcrypt

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View

from .validation import validate_password
from .models     import Posting


class PostingDetailView(View):
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
                    title   = data["title"],
                    context = data["context"],
                )
                return JsonResponse({"message": "UPDATED"}, status=201)

            hashed_password  = bcrypt.hashpw(psword.encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')

            Posting.objects.create(
                title   = title,
                context = context,
                psword  = decoded_password
            )

            return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 201)
        
        except KeyError:
            return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

        except ValidationError as e:
            return JsonResponse({'MESSAGE' : (e.message)}, status = 400)

    def delete(self, request):
        try:
            data        = json.loads(request.body)
            user_psword = data.get('psword')
            posting_id  = data.get('posting_id')
            posting     = Posting.objects.get(id=posting_id)

            encoded_user_psword = user_psword.encode('utf-8')
            encoded_db_psword   = posting.psword.encode('utf-8')

            if not bcrypt.checkpw(encoded_user_psword, encoded_db_psword):
                return JsonResponse({'MESSAGE' : 'INVALID_PASSWORD'}, status = 401)

            posting.delete()

            return JsonResponse({"message": "DATA_DELETED"}, status=204)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except Posting.DoesNotExist:
            return JsonResponse({"message": "POSTING_DOES_NOT_EXIST"}, status=400)