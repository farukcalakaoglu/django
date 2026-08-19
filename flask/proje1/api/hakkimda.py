from flask import Flask,Blueprint,Response

hakkimdaUser=Blueprint(
    "hakkimda",
    __name__,
    url_prefix="/api/hakkimda/"
    )


@hakkimdaUser.route("/hakkimda/")
def hakkimda():
    return Response("hakkımda sayfası")

@hakkimdaUser.route("/")
def index():
    return Response("hakkımda index sayfa")