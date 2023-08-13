import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import pandas as pd

@pytest.fixture()
def setup(request,browser):
    if browser=="chrome":
        opt = Options()

        opt.add_experimental_option("debuggerAddress", "localhost:9988")
        driver=webdriver.Chrome(executable_path="C:\\Users\\ashis\\PycharmProjects\\pythonProject4\\chromedriver.exe",chrome_options=opt)
    elif browser=="edge":
        driver=webdriver.Edge(executable_path="C:\\Users\\ashis\\Desktop\\msedgedriver.exe")

    A = "C:\\Users\\ashis\\Downloads\\BUCRP-10-JUL.xlsx"
    data = pd.read_excel(A, dtype=str)
    E = data[["Req ID", "Line", "Item", "Req Qty", "Price", "Supplier", "Supplier.1", "Project", "Ship To"]]
    o = E["Req ID"].unique()
    L = E.groupby("Req ID")
    M = []
    excel = []
    for dat in L:
        M.append(list(dat))
    for tables in o:
        J = L.get_group(tables)
        excel.append(J)

    wait = WebDriverWait(driver, 10)
    a=ActionChains(driver)
    request.cls.excel=excel
    request.cls.a=a
    request.cls.driver=driver
    request.cls.wait =wait

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")