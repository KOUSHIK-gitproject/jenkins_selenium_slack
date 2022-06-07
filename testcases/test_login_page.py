import sys
import os, pytest
conf_path = os.getcwd()
sys.path.append(conf_path)
sys.path.append(conf_path.replace(r'\testcases', '') + r'\lib_folder')
from lib_folder.login_page import Login, UserManagement, InvitationManagement, Log_viewer


class TestUserManagement:

    def test_create_user(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.click_create_new_button():
            if user_mgnt_obj.fill_user_details() and user_mgnt_obj.click_save_button() and user_mgnt_obj.user_create_status():
                status = True
        assert status

    def test_update_user(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.search_user() and user_mgnt_obj.edit_user():
            status = user_mgnt_obj.update_user_details() and user_mgnt_obj.click_update_save_button() and user_mgnt_obj.user_create_status()
        assert status

    def test_deactivate_user(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.validate_settings_modal_tab():
            status = user_mgnt_obj.deactivate_user()
        assert status

    def test_activate_user(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.validate_settings_modal_tab():
            status = user_mgnt_obj.activate_user()
        assert status

    def test_delete_user(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.validate_settings_modal_tab():
            status = user_mgnt_obj.deleteUser()
        assert status

    def test_refresh_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.refresh():
            status = True
        assert status

    def test_toggle_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.toggle():
            status = True
        assert status

    def test_sort_Email_Address_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.sort_Email_Address():
            status = True
        assert status

    def test_sort_First_Name_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.sort_First_Name():
            status = True
        assert status

    def test_sort_Last_Name_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.sort_Last_Name():
            status = True
        assert status

    def test_sort_Status_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.sort_Status():
            status = True
        assert status

    def test_sort_Verified_Status_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.sort_Verified_Status():
            status = True
        assert status

    def test_Plus_btn_option(self, user_mgnt_obj):
        status = False
        if user_mgnt_obj.plus_btn():
            status = True
        assert status


class TestInvitationManagement:

    def test_invite_user(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.click_Invitation_management_option():
            if invt_mgnt_obj.click_invite_user_button():
                if invt_mgnt_obj.fill_user_details():
                    status = invt_mgnt_obj.click_save_button() and invt_mgnt_obj.user_create_status()
        assert status

    def test_download_template(self, invt_mgnt_obj):
        status = invt_mgnt_obj.download_template()
        if status:
            self.extracted_email = status
            assert True
        else: assert False

    def test_upload_template(self, invt_mgnt_obj):
        assert invt_mgnt_obj.upload_template()

    def test_delete_user(self, user_mgnt_obj, invt_mgnt_obj):
        status = False
        if user_mgnt_obj.delete_cdc_user(email="example@example.com"):
            if invt_mgnt_obj.click_Invitation_management_option():
                status = invt_mgnt_obj.delete_user()
        assert status

    def test_refresh_option(self, invt_mgnt_obj):
        if invt_mgnt_obj.click_Invitation_management_option():
            status = False
            if invt_mgnt_obj.refresh():
                status = True
            assert status

    def test_toggle_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.toggle():
            status = True
        assert status

    def test_sort_Email_Address_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.sort_Email_Address():
            status = True
        assert status

    def test_sort_Tenants_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.sort_Tenants():
            status = True
        assert status

    def test_sort_Invited_date_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.sort_Invited_date():
            status = True
        assert status

    def test_sort_Invitation_expiry_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.sort_Invitation_expiry():
            status = True
        assert status

    def test_sort_Invitation_Status_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.sort_Invitation_status():
            status = True
        assert status

    def test_Plus_btn_option(self, invt_mgnt_obj):
        status = False
        if invt_mgnt_obj.plus_btn():
            status = True
        assert status

class TestLogViewer:

    def test_logviewer(self, log_view_obj):
        status = log_view_obj.log_viewer()
        assert status