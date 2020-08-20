from src.errors import RequestError


def validate_body_existence(body: dict) -> None:
    if body is None:
        raise RequestError('Request no body', 409)


def validate_field_existence(body: dict, field_name: str) -> None:
    if field_name not in body:
        raise RequestError(f'Body do not have {field_name} field', 409)
