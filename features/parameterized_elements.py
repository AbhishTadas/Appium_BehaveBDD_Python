from config import CONFIG

PARAMETERIZED_XPATHS = {
    'app_by_content_desc': '//android.widget.TextView[@content-desc="{appname}"]',
    'discovered_feed_option': f'//android.widget.TextView[@resource-id="{CONFIG["chrome_menu_item_resource_id"]}" and @text="{{option}}"]',
    'image_button_by_content_desc': '//android.widget.ImageButton[@content-desc="{element}"]',
}
