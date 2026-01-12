from rest_framework.decorators import api_view
from rest_framework.response import Response
from auth_app.permissions import HasPermission

@api_view(['GET'])
def list_projects(request):
    return Response([
        {"id": 1, "name": "Project Alpha"},
        {"id": 2, "name": "Project Beta"}
    ])

list_projects.permission_classes = [HasPermission]
list_projects.required_permission = 'project:read'

@api_view(['POST'])
def create_project(request):
    return Response({"message": "Project created"}, status=201)

create_project.permission_classes = [HasPermission]
create_project.required_permission = 'project:write'