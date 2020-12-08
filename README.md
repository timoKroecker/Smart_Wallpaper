# Smart_Wallpaper

This project is aggregates and scrapes diverse content,
displays it in an appealing background image
and sets that image as a new desktop wallpaper.

Aggregated content:
    Birthdays:
        The repository provides a directory for saving birthdays of family and friends.
        The wallpaper will display all birthdays of the next 31 days.
        Birthdays of the current day will be highlighted.
    Expences:
        The repository will provide a directory for saving monthy expences.
        The wallpaper will display all expences of the current month and year,
        divided into fixed costs, groceries, household, leisure and transport.
    News:
        Current news headlines will be scraped
        from various websites such as focus.de or spiegel.de.
        The headlines will first be given a score
        through the occurance of headwords
        and second be ranked by that score.
        the four highest ranking headlines will the be displayed.
    Weather:
        Informations about the current temperature (day/night), weather conditions,
        and times of dawn and dusk will be scraped from the web
        and displayed.
        Note: the project always displays local the informations for Augsburg, Germany.

Tipps:
    It is recommended to set a scheduled task (e.g. on Windows Task Scheduler)
    for the execution of the program on your machine.
    Both a timed schedule at midnight and a schedule on every login
    are very helpful to keep the content updated.