from flask import render_template
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return (
        render_template(
            # "/components/_blank.html",
            "/errors/error.html",
            message="403. Sorry, this page unavailable.",
        ),
        403,
    )


@main.app_errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "errors/error.html",
            message="404. Page Not Found.",
        ),
        404,
    )


@main.app_errorhandler(500)
def internal_server_error(e):
    return (
        render_template(
            "errors/error.html",
            message="500. Oops. Something has gone wrong.",
        ),
        500,
    )
