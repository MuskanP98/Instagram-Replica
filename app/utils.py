from datetime import datetime, timedelta
import pytz
from flask import flash, redirect, url_for
from flask_login import current_user

def allowed_file(filename):
    """
    Checks if the given file has an allowed file extension.
    """
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_image_to_gcs(file, bucket, blob_name):
    """
    Uploads a file to Google Cloud Storage.
    """
    from google.cloud import storage
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(blob_name)
    blob.upload_from_file(file)
    blob.make_public()
    return blob.public_url

def flash_errors(form):
    """
    Flashes form validation errors as flash messages.
    """
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field}: {error}", "danger")

def validate_timezone(timezone):
    """
    Validates a timezone string.
    """
    try:
        pytz.timezone(timezone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False

def get_local_time(dt, tz):
    """
    Converts a datetime object to the given timezone, and returns a formatted string representation of the local time.
    """
    if not tz:
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    local_tz = pytz.timezone(tz)
    local_dt = dt.astimezone(local_tz)
    return local_dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")

def redirect_back(default="index"):
    """
    Redirects the user back to the page they came from, or to the default page if the referrer is not set or is not
    part of the application.
    """
    referrer = request.headers.get("Referer")
    if not referrer or url_parse(referrer).netloc != "":
        return redirect(url_for(default))
    return redirect(referrer)
