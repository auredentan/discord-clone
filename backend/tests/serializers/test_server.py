from src.entities.server import PydanticServerMember

from src.infrastructure.adapters.database.tables.server import Server
from src.infrastructure.adapters.database.tables.server import ServerMember

from src.use_cases.serializers.server_serializer import server_sqlalchemy_to_pydantic


def test_server_sqlalchemy_to_pydantic():

    user_id = "1"
    server_id = "100"
    members = [
        ServerMember(id="201", name="", roles=[], user_id=user_id, server_id=server_id)
    ]

    expected_server_name = "server_name"
    db_model: Server = Server(id="200", name=expected_server_name, members=members)

    serialized = server_sqlalchemy_to_pydantic(db_model)

    assert serialized
    assert serialized.members and len(serialized.members) == len(members)
    assert serialized.name == expected_server_name

    first_expected_member = members[0]
    first_seria_member = serialized.members[0]
    assert isinstance(first_seria_member, PydanticServerMember)
    assert first_expected_member.id == first_seria_member.id