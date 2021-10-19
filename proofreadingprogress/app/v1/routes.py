from flask import Blueprint
from flask import request
from flask_cors import cross_origin
from middle_auth_client import auth_required
from proofreadingprogress.app import common
import pandas as pd

bp = Blueprint(
    "proofreadingprogress_v1", __name__, url_prefix=f"/{common.__url_prefix__}/api/v1"
)

# -------------------------------
# ------ Access control and index
# -------------------------------


@bp.route("/")
@bp.route("/index")
def index():
    return common.index()


@bp.route("/query", methods=["GET"])
def query():
    return common.query()


@bp.route("/user", methods=["GET"])
def user():
    return common.user()


@bp.route("/publish", methods=["GET"])
def publish():
    return common.publish()


@bp.route("/table", methods=["GET", "POST"])
def table():
    return common.table()


@bp.route("/<name>.js", methods=["GET"])
def scripts(name):
    return common.getScripts(name + ".js")


@bp.route("/<name>.css", methods=["GET"])
def style(name):
    return common.getStyles(name + ".css")


@bp.route
def home():
    return common.home()


# -------------------------------
# ------ Measurements and Logging
# -------------------------------


@bp.before_request
@auth_required
def before_request():
    return common.before_request()


@bp.after_request
def after_request(response):
    return common.after_request(response)


@bp.errorhandler(Exception)
def internal_server_error(e):
    return common.internal_server_error(e)


@bp.errorhandler(Exception)
def unhandled_exception(e):
    return common.unhandled_exception(e)


# -------------------
# ------ Applications
# -------------------


@bp.route("/qry/", methods=["GET"])
def pass_through():
    return common.apiRequest(request.args)


@bp.route("/pub/", methods=["GET"])
def publish_neurons():
    return common.publish_neurons(request.args)


@bp.route("/pubreq/", methods=["GET"])
def publish_request():
    return common.publishRequest(request.args)


@bp.route("/pubdmp/", methods=["GET"])
def publish_dump():
    return common.publishDump()
