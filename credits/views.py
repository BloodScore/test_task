from django.http import HttpResponse

from .models import CreditRequest


def get_manufacturers_ids(request, contract_id):
    try:
        credit_request = CreditRequest.objects.prefetch_related('products__manufacturer').get(pk=contract_id)
    except Exception:
        return HttpResponse('Matching contract is not found!')

    ids = set([product.manufacturer.id for product in credit_request.products.all()])

    response = '<html><body><table>'

    for i in ids:
        response += f'<tr><td>{i}</td></tr>'

    response += '</table></body></html>'

    return HttpResponse(response)
