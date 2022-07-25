class Locators:
    # login page objects
    user_name_textbox_id = 'user-name'
    password_textbox_id = 'password'
    login_button_id = 'login-button'
    error_message_xpath = '//*[@data-test="error"]'
    # header page objects
    hamburger_menu_id = 'react-burger-menu-btn'
    inventory_sidebar_id = 'inventory_sidebar_link'
    logout_sidebar_id = 'logout_sidebar_link'
    shopping_cart_class = '//*[@class="shopping_cart_badge"]'
    # footer page objects
    twitter_logo_xpath = '//*[@class="social_twitter"]'
    facebook_logo_xpath = '//*[@class="social_facebook"]'
    linkedin_logo_xpath = ''
    # inventory page objects
    inventory_items = '//div[@class="inventory_item"]'
    inventory_item_name_class = './/div[@class="inventory_item_name"]'
    inventory_item_desc_class = './/div[@class="inventory_item_desc"]'
    inventory_item_price_class = './/div[@class="inventory_item_price"]'
    inventory_item_img_class = './/child::img[@class="inventory_item_img"]'
    inventory_item_btn_class = './/*[@class="pricebar"]//child::button'
    # details page objects
    details_back_to_products_id = 'back-to-products'
    details_name_class = '//*[@class="inventory_details_name large_size"]'
    details_description_class = '//*[@class="inventory_details_desc large_size"]'
    details_price_class = '//*[@class="inventory_details_price"]'
    details_img_class = '//*[@class="inventory_details_img"]'
    details_button_class = '//*[@class="btn btn_secondary btn_small btn_inventory"]'
