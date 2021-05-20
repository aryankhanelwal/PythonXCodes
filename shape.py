class rectangle:
    def SetData(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        self.area = self.l*self.w
    def perimeter(self):
        self.perimeter = 2*(self.l+self.w)
    def show(self):
        if z == 'area':
            print('area of rectangle is', self.area)
        elif z == 'perimeter':
            print('perimeter of rectangle is',self.perimeter)

class circle:
    def SetData(self,r):
        self.r = r
    def area(self):
        self.area = 3.14*self.r*self.r
    def circumference(self):
        self.circumference = 2*3.14*self.r
    def show(self):
        if z == 'area':
            print('area of circle is',self.area)
        elif z == 'circumference':
            print('circumference of circle is',self.circumference)
class square:
    def SetData(self,a):
        self.a = a 
    def area(self):
        self.area = self.a*self.a
    def perimeter(self):
        self.perimeter = 4*self.a
    def show(self):
        if z == 'area':
            print('area of circle is',self.area)
        elif z == 'perimeter':
            print('perimeter of circle is',self.perimeter)
class traingle:
    def SetData(self,b,h,side1,side2):
        self.b = b
        self.h = h
        self.side1 = side1
        self.side2 = side2
    def area(self):
        self.area = 0.5*self.b*self.h
    def perimeter(self):
        self.perimeter = self.side1+self.side2+self.b
    def show(self):
        if z == 'area':
            print('area of traingle is',self.area)
        elif z == 'perimeter':
            print('perimeter of traingle is',self.perimeter)
class sphere:
    def SetData(self,r):
        self.r = r
    def volume(self):
        self.volume = 1.33*self.r*self.r
    def SA(self):
        self.SA = 4*3.14*self.r*self.r
    def show(self):
        if z == 'volume':
            print('volume if sphere is',self.volume)
        elif z == 'surface Area':
            print('surface area of sphere is',self.SA)
t=100
while(t>0):

    print("\n1.rectangle\n2.circle\n3.square\n4.traingle\n5.Sphere")
    choice = int(input("enter choice"))
    if choice == 1:
        q = rectangle()
        z = input("enter(area or perimeter)")
        q.SetData(int(input("enter length")),int(input("enter width")))
        q.area()
        q.perimeter()
        q.show()    
    elif choice == 2:
        w=circle()
        z = input("enter(area or circumference)")
        w.SetData(int(input("enter radius")))
        w.area()
        w.circumference()
        w.show()
    elif choice == 3:
        e = square()
        z=input('enter(area or perimeter)')
        e.SetData(int(input("enter side ")))
        e.area()
        e.perimeter()
        e.show()
    elif choice == 4:
        r = traingle()
        z=input('enter(area,perimeter)')
        r.SetData(int(input("enter base ")),int(input("enter height ")),int(input("enter side1 ")),int(input("enter side2 ")))
        r.area()
        r.perimeter()
        r.show()
    elif choice == 5:
        t = sphere()
        z=input('enter(volume or SA)')
        t.SetData(int(input("enter radius ")))
        t.volume()
        t.SA
        t.show()
    
       

