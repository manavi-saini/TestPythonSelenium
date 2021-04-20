class Locators:

    # Login page Locators
    username = "txtUsername"
    password = "txtPassword"
    loginButton = "btnLogin"

    # Home page Locators
    pim_module_menu_link = "menu_pim_viewPimModule"
    add_employee_menu_link = "menu_pim_addEmployee"
    admin_menu_link = "menu_admin_viewAdminModule"
    adduser_button = "btnAdd"
    username_textbox = "searchSystemUser_userName"
    searchbutton = "searchBtn"
    searcheduser_table = "//table[@id='resultTable']//tbody//tr[1]/td[2]"

    # Add Employee Page
    firstname_textbox = "firstName"
    lastname_textbox = "lastName"
    savebutton = "btnSave"

    # Add User Page
    userrole_dropdown = "systemUser_userType"
    employeename_textbox = "systemUser_employeeName_empName"
    usrname_textbox = "systemUser_userName"
    statusdropdown = "systemUser_status"
    pwd_textbox = "systemUser_password"
    confpwd_textbox = "systemUser_confirmPassword"

    # Employee Details page
    personal_details_header = "//div[@class='personalDetails']//h1"
    add_attachment = "btnAddAttachment"
    upload_file_input = "ufile"
    save_upload = "btnSaveAttachment"