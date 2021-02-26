Установка зависимостей
`pip install -r requirements.txt`

Запуск хаба Selenium Grid
`java -jar selenium-server-standalone-3.141.59.jar -role hub -port 4445`

Запуск ноды Selenium Grid
`java "-Dwebdriver.chrome.driver=D:\Selenium_GRID\chromedriver.exe" -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4445/grid/register -browser "browserName=chrome,maxInstances=3,platform=WINDOWS" -port 5557`

Запуск теста с сохранением отчета
`pytest --alluredir=./allure-results .\Tests\TestCase1.py`

Просмотр отчетов
`allure serve .\allure-results\`