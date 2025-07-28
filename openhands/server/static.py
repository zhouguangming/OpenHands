from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        try:
            return await super().get_response(path, scope)
        except HTTPException as exc:
            # For 404 errors (file not found), serve index.html for SPA routing
            if exc.status_code == 404:
                return await super().get_response('index.html', scope)
            # Re-raise other HTTP exceptions (401, 405, etc.)
            raise
