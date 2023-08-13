import pytest


from PageObjects.psoftmod import functions


@pytest.mark.usefixtures("setup")

class Test_01:
    #k = 27


    def test_start(self):
        global supplier

        self.lp=functions(self.driver,self.a,self.wait,self.excel)
        for supp in range(len(self.excel)):
            if supp ==1:
                break
            supplier=self.excel[supp]
            print(supplier)
            self.test_supplier()


    def test_supplier(self):
        self.lp = functions(self.driver, self.a, self.wait, self.excel)
        global i
        for i in range(len(supplier)):

            if i==1:
                break
            Q = supplier.iloc[i, 5]
            print(Q)
            self.lp.SupplierField(Q)

            self.test_requisition()


    def test_requisition(self):
         global P
         self.lp = functions(self.driver, self.a, self.wait, self.excel)
         for req in range(len(supplier["Req ID"])):
             if req ==1:
                 break

             P = supplier.iloc[req, 0]
             self.lp.Requisition(P)
             print(P)
         self.test_defaultsettings()


    def test_defaultsettings(self):
        self.lp = functions(self.driver, self.a, self.wait, self.excel)
        for shipto in range(len(supplier)):

            if shipto == 1:
                break
            S = supplier.iloc[shipto, 8]
            T="FCA"
            U="Services only"


            self.lp.Defaultsetting(S,T,U)


    def test_Poput(self):
        self.lp = functions(self.driver, self.a, self.wait, self.excel)
        self.lp.Popup()


    def test_Save(self):
        self.lp = functions(self.driver, self.a, self.wait, self.excel)
        Q=supplier.iloc[i, 7]
        self.lp.Save(P,Q)


    def test_add(self):
        self.lp = functions(self.driver, self.a, self.wait, self.excel)
        self.lp.addagain()






