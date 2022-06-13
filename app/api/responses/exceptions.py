from responses.error_response import ErrorResponse

exceptions = {
    404: lambda _request, _exception: ErrorResponse(
        "Resource not found",
        "The endpoint you requested does not seem to exist.",
        "endpointNotFoundException",
        404,
    ),
    500: lambda _request, _exception: ErrorResponse(
        "Internal server error",
        "Something went wrong internally try sending your request again.",
        "internalServerException",
        500,
    ),
}
