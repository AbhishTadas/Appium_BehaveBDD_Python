from config import CONFIG

NORMAL_XPATHS = {
    'chrome_menu_item': f'//android.widget.TextView[@resource-id="{CONFIG["chrome_menu_item_resource_id"]}"]',
    'options_for_discover': '//android.widget.ImageButton[@content-desc="Options for Discover"]',
}
