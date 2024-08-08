from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import AuthInSchema, AuthOutSchema, TokenInSchema, TokenOutSchema
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import AuthService
from core.apps.customers.services.codes import DjangoCacheCodeService
from core.apps.customers.services.customer import ORMCustomerService
from core.apps.customers.services.senders import DummySenderService

router = Router(tags=['Customers'])


@router.post('auth', response=ApiResponse[AuthOutSchema], operation_id='authorize')
def auth_hendler(
        request: HttpRequest,
        schema: AuthInSchema,
) -> ApiResponse[AuthOutSchema]:
    service = AuthService(
        customer_service=ORMCustomerService(),
        codes_service=DjangoCacheCodeService(),
        sender_service=DummySenderService()
    )
    service.authorize(schema.phone)
    return ApiResponse(data=AuthOutSchema(
        message=f'Code is sent to: {schema.phone}',
    ))


@router.post('confirm', response=ApiResponse[TokenOutSchema], operation_id='confirmCode')
def auth_hendler(
        request: HttpRequest,
        schema: TokenInSchema,
) -> ApiResponse[TokenOutSchema]:
    service = AuthService(
        customer_service=ORMCustomerService(),
        codes_service=DjangoCacheCodeService(),
        sender_service=DummySenderService()
    )

    try:
        token = service.confirm(schema.code, schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=404,
            message=exception.message,
        )

    return ApiResponse(data=TokenOutSchema(token=token))