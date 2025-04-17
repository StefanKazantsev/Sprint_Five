#все локаторы

class AllLocators:

    login_in_acc_button = ".//button[text()='Войти в аккаунт']"
    input_email = ".//input[@name='name']"
    input_pass =  ".//input[@name='Пароль']"
    login_button = ".//button[text()='Войти']"
    button_logout = ".//button[text()='Выход']"
    login_page_text = ".//h2[text()='Вход']"

    page_login_text_vhod = ".//h2[text()='Вход']"

    page_main_button_get_order = ".//button[text()='Оформить заказ']"
    main_page_all_list = ".//div[@class='BurgerIngredients_ingredients__menuContainer__Xu3Mo']"
    main_page_button_acc = ".//p[text()='Личный Кабинет']"
    main_page_button_login = ".//button[text()='Войти в аккаунт']"
    main_page_button_sous = ".//span[text()='Соусы']"
    main_page_section_sous = ".//h2[text()='Соусы']"
    main_page_button_nachinka = ".//span[text()='Начинки']"
    main_page_section_nachinka = ".//h2[text()='Начинки']"
    main_page_button_bulki = ".//span[text()='Булки']"
    main_page_section_bulki = ".//h2[text()='Булки']"

    page_accont_button_save = ".//button[text()='Сохранить']"
    page_account_button_logo = "(.//a[@href='/'])[2]"
    page_account_button_constructor = ".//p[text()='Конструктор']"
    account_page_text_profile = ".//a[text()='Профиль']"

    page_register_button_login = ".//a[text()='Войти']"
    page_register_input_name = "(.//input[@type='text'])[1]"
    page_register_input_email =" (.//input[@type='text'])[2]"
    page_register_input_pass = ".//input[@type='password']"
    page_register_button_registration = ".//button[text()='Зарегистрироваться']"
    page_register_error_pass_text = ".//p[text()='Некорректный пароль']"