import pytest
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Эта штука слушает результаты каждого теста
    outcome = yield
    rep = outcome.get_result()
    
    # Если тест упал
    if rep.when == "call" and rep.failed:
        # Пытаемся достать объект page из фикстур теста
        page = item.funcargs.get("page")
        if page:
            # Делаем скриншот и крепим его к Allure
            allure.attach(
                page.screenshot(),
                name="Screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )