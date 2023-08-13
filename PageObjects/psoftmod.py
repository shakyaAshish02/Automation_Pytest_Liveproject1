
from selenium.webdriver.support import expected_conditions as con
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from Utilities.Customlogger import logclass


class functions:
    BaseFrame = "//iframe[@id='ptifrmtgtframe']"
    supplierfield = '//*[@id="PO_HDR_VENDOR_ID$24$"]'
    requisitiontab = '//*[@id="PO_COPY_TMPLT_W_COPY_PO_FROM"]'
    ReqID = "//input[@id='PO_REQ_WRK_REQ_ID']"
    ReqSearch = "//input[@id='PO_REQ_WRK_REQ_SELECT']"
    PoDefaults = '//*[@id="PO_PNLS_WRK_GOTO_DEFAULTS"]'
    BaseFrame2 = "//iframe[starts-with(@id,'ptModFrame_')]"
    ShipTo = "//*[@id='PO_DFLT_TBL_SHIPTO_ID']"
    FreightTerms = "//*[@id='PO_DFLT_TBL_FREIGHT_TERMS']"
    ShippingType = '//*[@id="OI_PO_DFLT_WRK_OI_NAMED_PLACE"]'
    Location = "//*[@id='LOCATION$0']"
    Savedefaults = "//div[@id='win0divPSTOOLBAR']//a[1]"
    PopupOk = "//*[@id='#ICYes']"
    PopupFrame = "//iframe[starts-with(@id, 'ptModFrame_')]"
    Markall = "//a[@id='PO_PNLS_WRK2_MARK_ALL_LINES_FLG$13$']"
    MarkOk = "//*[@id='#ICSave']"
    PoRefrence = "//input[@id='PO_HDR_PO_REF']"
    SavePo = "//input[@id='#ICSave']"
    GlobalAdd = "// a[@ id='pthnavbccrefanc_EP_PURCHASE_ORDER_GBL']"
    Add = "//input[@id='PTS_CFG_CL_WRK_PTS_ADD_BTN']"
    log=logclass.getthelogs()

    def __init__(self, driver, a, wait,excel):
        self.driver = driver
        self.a = a
        self.wait = wait
        self.excel=excel
    def browe(self,pak):
        #self.driver.get("https://"+str(p))
        print(pak)

    def SupplierField(self, supplierID):
        self.log.info("supplier field test started")
        self.driver.switch_to.default_content()
        frame1 = self.wait.until(con.presence_of_element_located((By.XPATH, self.BaseFrame)))
        self.driver.switch_to.frame(frame1)
        suppfield = self.wait.until(con.presence_of_element_located((By.XPATH, self.supplierfield)))
        suppfield.send_keys(supplierID)
        time.sleep(2)

    def Requisition(self, req):
        self.log.info("requisition field test started")

        drop = self.wait.until(con.presence_of_element_located((By.XPATH, self.requisitiontab)))
        drp = Select(drop)
        time.sleep(1)
        drp.select_by_value("R")
        time.sleep(2)
        Req = self.wait.until(con.presence_of_element_located((By.XPATH, self.ReqID))).send_keys(req)
        self.wait.until(con.presence_of_element_located((By.XPATH, self.ReqSearch))).click()

    def Defaultsetting(self, shipto, incoterms, shptype):
        self.log.info("default test started")
        self.driver.switch_to.default_content()
        frame1 = self.wait.until(con.presence_of_element_located((By.XPATH, self.BaseFrame)))
        self.driver.switch_to.frame(frame1)

        defaults = self.wait.until(con.presence_of_element_located((By.XPATH, self.PoDefaults))).click()

        self.driver.switch_to.default_content()
        self.wait.until(con.presence_of_element_located((By.XPATH, self.BaseFrame2)))
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.BaseFrame2))
        self.wait.until(con.presence_of_element_located((By.XPATH, self.ShipTo))).send_keys(shipto)
        self.wait.until(con.presence_of_element_located((By.XPATH, self.FreightTerms))).send_keys(incoterms)
        self.wait.until(con.presence_of_element_located((By.XPATH, self.ShippingType))).send_keys(shptype)
        self.wait.until(con.presence_of_element_located((By.XPATH, self.Location))).clear()
        self.wait.until(con.presence_of_element_located((By.XPATH, self.Location))).send_keys(shipto)
        time.sleep(2)
        self.wait.until(con.presence_of_element_located((By.XPATH,self.Savedefaults))).click()
        self.driver.switch_to.default_content()

    def Popup(self):
        self.log.info("popup field test started")

        self.wait.until(con.presence_of_element_located((By.XPATH, self.PopupOk))).click()

        self.wait.until(con.presence_of_element_located((By.XPATH, self.PopupFrame)))
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.PopupFrame))

        self.wait.until(con.presence_of_element_located((By.XPATH, self.Markall))).click()

        self.wait.until(con.presence_of_element_located((By.XPATH, self.MarkOk))).click()
        self.driver.switch_to.default_content()

    def Save(self, r, ch):
        self.log.info("save field test started")
        framel = self.wait.until(con.presence_of_element_located((By.XPATH, self.BaseFrame)))
        self.driver.switch_to.frame(framel)
        time.sleep(3)
        T = "REQ" + ":" + str(int(r)) + " " + "CH" + ":" + str(int(ch))
        self.wait.until(con.presence_of_element_located((By.XPATH, self.PoRefrence))).send_keys(T)
        self.wait.until(con.presence_of_element_located((By.XPATH, self.SavePo))).click()
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(2)

    def addagain(self):
        self.log.info("add field test started")
        self.wait.until(con.presence_of_element_located((By.XPATH, self.GlobalAdd))).click()
        frame1 = self.wait.until(con.presence_of_element_located((By.XPATH, self.BaseFrame)))
        self.driver.switch_to.frame(frame1)
        time.sleep(3)
        self.wait.until(con.element_to_be_clickable((By.XPATH, self.Add))).click()