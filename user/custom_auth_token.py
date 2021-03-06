from user.serializer import CustomAuthTokenSerializer
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema


class CustomAuthToken(auth_views.ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = CustomAuthToken.as_view()
