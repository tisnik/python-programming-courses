HTTP_RE = re.compile(
    r"^(?:https://[^/]+\.s3\.amazonaws\.com/[0-9a-zA-Z/\-]+|"
    r"https://s3\.[0-9a-zA-Z\-]+\.amazonaws\.com/[0-9a-zA-Z\-]+/[0-9a-zA-Z/\-]+|"
    r"http://minio:9000/insights-upload-perma/[0-9a-zA-Z\.\-]+/[0-9a-zA-Z\-]+)\?"
    r"X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[^/]+$"
)


def get(self, src):
    """Download a file from HTTP server and store it in a temporary file."""
    if src is None or not HTTP_RE.fullmatch(src):
        raise DataPipelineError(f"Invalid URL format: {src}")
