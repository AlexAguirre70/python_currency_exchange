class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
    return f"Value Converted to {self.unit}"
  #add magic methods here
  def __repr__(self):
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
    return "Currency({},'{}')".format(str(round(self.value,2)),self.unit)
    
  
  def __str__(self):
    #This method returns the same value as __repr__(self).
    return "Currency({},'{}')".format(str(round(self.value,2)),self.unit)
    
  def __add__(self,other):
    #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
    
    if isinstance(self,Currency) and isinstance(other,Currency):
      other.changeTo(f"{self.unit}")
      return f"The sum is "+ str(round(self.value + other.value,2))+f" in {self.unit} "
    elif isinstance(self,Currency) and isinstance(other,(float, int)):
      v3=Currency(other,"USD")
      v3.changeTo(f"{self.unit}")
      return f"The sum is "+ str(round(self.value + v3.value,2))+f" in {self.unit} "
    # except:     
    #   if isinstance(self,(float,int)) and isinstance(other,Currency):
    #     v4=Currency(self,"USD")
    #     other.changeTo(f"{v3.unit}")
    #     return f"The sum is "+ str(round(v3.value + other.value,2))+f" in {v3.unit} "

      
  def __sub__(self,other):
    #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
    if isinstance(self,Currency) and isinstance(other,Currency):
      other.changeTo(f"{self.unit}")
      return f"The difference is "+ str(round(self.value - other.value,2))+f" in {self.unit} "
    elif isinstance(self,Currency) and isinstance(other,(float, int)):
      v3=Currency(other,"USD")
      v3.changeTo(f"{self.unit}")
      return f"The difference is "+ str(round(self.value - v3.value,2))+f" in {self.unit} "    
  

v1 = Currency(23.43, 'EUR')
v2 = Currency(19.9725, 'USD')

print(v1.changeTo('USD'))
print(v2.__repr__())
print(v2.__str__())

print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(v2 + 3) # an int or a float is considered to be a USD value
print(v1 - v2) # an int or a float is considered to be a USD value
print(v2 - v1) # an int or a float is considered to be a USD value
print(v1 - 3) # an int or a float is considered to be a USD value
print(v2 - 3) # an int or a float is considered to be a USD value
print(3 + v1.value)
print(30 - v2.value) 

# when sending input as an integer first and then passing the object, I received an unsupported error for + operand. I suspect because an integer is not of a Currency class, so it cannot access the __add__ or __sub__ methods.  The only other solution I can think of is to convert the input to the object prior to calling the methods, or simply asking for the value itself of the object and it bypasses the class method call. 