from selenium.webdriver.common.by import By


class BlogPageLocators:
    ADD_POST_LINK = By.ID, 'new-post-link'
    POSTS_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post-link'