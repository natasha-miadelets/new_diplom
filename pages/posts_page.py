from pages.base_page import BasePage
from locators.Posts_Page_Locators import PostsPageLocators


class PostsPage(BasePage):

    def should_be_posts_page(self):
        posts_head_text = self.find_element(
            PostsPageLocators.LOCATOR_HEAD_TEXT).text
        assert posts_head_text == "Select post to change",\
            f'Select post to change not eq {posts_head_text}'

    def delete_post(self):
        self.find_element(PostsPageLocators.LOCATOR_FIRST_POST).click()
        self.find_element(PostsPageLocators.LOCATOR_DELETE_BUTTON).click()
        self.find_element(PostsPageLocators.LOCATOR_SURE_BUTTON).click()

    def go_to_main_page(self):
        self.find_element(PostsPageLocators.LOCATOR_VIEW_SITE_BUTTON).click()
