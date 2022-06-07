from lib_folder.login_page import Login, UserManagement, InvitationManagement
import pytest

@pytest.mark.usefixtures('setup')
class Obj_Helper:
    pass

class Helper(Obj_Helper):

    @property
    def login_obj(self):
        return Login(Obj_Helper)

    @property
    def user_mgnt_obj(self):
        return UserManagement(Obj_Helper)

    @property
    def inv_mgnt_obj(self):
        return InvitationManagement(Obj_Helper)


