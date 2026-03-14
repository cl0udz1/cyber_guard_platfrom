from app.core.permissions import can_manage_workspace, can_review_public_content


def test_workspace_management_roles() -> None:
    assert can_manage_workspace("org_owner") is True
    assert can_manage_workspace("org_admin") is True
    assert can_manage_workspace("analyst") is False


def test_review_roles() -> None:
    assert can_review_public_content("platform_admin") is True
    assert can_review_public_content("security_reviewer") is True
    assert can_review_public_content("viewer") is False
