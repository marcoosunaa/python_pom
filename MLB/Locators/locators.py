class Locators:
    # header page objects
    menu_logo_xpath = 'logo__link'
    menu_news_xpath = '//*[@data-nav-id="nav-top-item-news"]'
    menu_watch_xpath = '//*[@data-nav-id="nav-top-item-watch"]'
    menu_scores_xpath = '//*[@data-nav-id="nav-top-item-scores"]'
    menu_schedule_xpath = '//*[@data-nav-id="nav-top-item-schedule"]'
    menu_stats_xpath = '//*[@data-nav-id="nav-top-item-stats"]'
    menu_standings_xpath = '//*[@data-nav-id="nav-top-item-standings"]//*//a'
    menu_youth_xpath = '//*[@data-nav-id="nav-top-item-youth"]'
    menu_players_xpath = '//*[@data-nav-id="nav-top-item-players"]'
    # standings page objects
    AL_east_table_xpath = '//*[@id="regularSeason-division-201"]//*[@class="responsive-datatable__scrollable"]//tbody//tr'
    AL_central_table_xpath = '//*[@id="regularSeason-division-202"]//*[@class="responsive-datatable__scrollable"]//tbody//tr'
    AL_west_table_xpath = '//*[@id="regularSeason-division-200"]//*[@class="responsive-datatable__scrollable"]//tbody//tr'
    columns_xpath = './/td'
