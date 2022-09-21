#Python monitor generated using LamaConv
#This file stores the monitor that is used

class Monitor:
  def __init__(self, callback):
    self.state = "q6"
    self.output = None
    self.callback = callback

  
  
  def transit_to_q6(self):
    self.state = "q6"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q14(self):
    self.state = "q14"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q8(self):
    self.state = "q8"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q5(self):
    self.state = "q5"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q4(self):
    self.state = "q4"
    self.output = True
    self.callback(self.output)
  
  
  def transit_to_q13(self):
    self.state = "q13"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q0(self):
    self.state = "q0"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q12(self):
    self.state = "q12"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q3(self):
    self.state = "q3"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q15(self):
    self.state = "q15"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q10(self):
    self.state = "q10"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q1(self):
    self.state = "q1"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q9(self):
    self.state = "q9"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q7(self):
    self.state = "q7"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q11(self):
    self.state = "q11"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q2(self):
    self.state = "q2"
    self.output = None
    self.callback(self.output)
  

  
  def transit(self, assignment):


    if self.state == "q6":
      if (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q6()
      if (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q14()
      if (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]):
        self.transit_to_q8()
      if (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]):
        self.transit_to_q5()
      if (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]):
        self.transit_to_q4()
      if (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]):
        self.transit_to_q13()
      if (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]):
        self.transit_to_q0()
      if (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q12()
      if (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]):
        self.transit_to_q3()
      if (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]):
        self.transit_to_q15()
      if (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]):
        self.transit_to_q10()
      if (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q1()
      if (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]):
        self.transit_to_q9()
      if (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]):
        self.transit_to_q7()
      if (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]):
        self.transit_to_q11()
      if (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q2()
      return



    if self.state == "q14":
      if ((not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q14()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"])):
        self.transit_to_q5()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"])):
        self.transit_to_q4()
      if ((assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q0()
      if ((assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q12()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"])):
        self.transit_to_q1()
      if ((assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q7()
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q11()
      return



    if self.state == "q8":
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"])):
        self.transit_to_q4()
      if ((assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q8()
      if ((assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q5()
      if ((assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q3()
      return



    if self.state == "q5":
      if ((assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q4()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q5()
      return



    if self.state == "q4":
      self.transit_to_q4()
      return



    if self.state == "q13":
      if ((assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q8()
      if ((assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"])):
        self.transit_to_q5()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"])):
        self.transit_to_q4()
      if ((not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q13()
      if ((assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q0()
      if ((assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"])):
        self.transit_to_q3()
      if ((assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q9()
      if ((assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"])):
        self.transit_to_q11()
      return



    if self.state == "q0":
      if ((not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q0()
      if ((assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q5()
      if ((assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"])):
        self.transit_to_q11()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"])):
        self.transit_to_q4()
      return



    if self.state == "q12":
      if ((assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"])):
        self.transit_to_q5()
      if ((assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q12()
      if ((assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"])):
        self.transit_to_q1()
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q4()
      return



    if self.state == "q3":
      if ((not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q3()
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"])):
        self.transit_to_q4()
      return



    if self.state == "q15":
      if ((assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"])):
        self.transit_to_q3()
      if ((assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q15()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q4()
      if ((assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q1()
      return



    if self.state == "q10":
      if ((assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"])):
        self.transit_to_q4()
      if ((assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"])):
        self.transit_to_q3()
      if ((assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"])):
        self.transit_to_q15()
      if ((not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q10()
      if ((assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q1()
      if ((assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q9()
      if ((assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q7()
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q11()
      return



    if self.state == "q1":
      if ((assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q4()
      if ((assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q1()
      return



    if self.state == "q9":
      if ((assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q9()
      if ((assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q11()
      if ((assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"])):
        self.transit_to_q3()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"])):
        self.transit_to_q4()
      return



    if self.state == "q7":
      if ((assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"])):
        self.transit_to_q4()
      if ((assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q7()
      if ((assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q1()
      if ((assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q11()
      return



    if self.state == "q11":
      if ((assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q11()
      if ((assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q4()
      return



    if self.state == "q2":
      if ((assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"])):
        self.transit_to_q8()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q5()
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"])):
        self.transit_to_q4()
      if ((assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q12()
      if ((assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"])):
        self.transit_to_q3()
      if ((assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q15()
      if ((assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q1()
      if ((not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q2()
      return


