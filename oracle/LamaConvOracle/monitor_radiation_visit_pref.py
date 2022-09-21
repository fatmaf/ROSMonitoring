#Python monitor generated using LamaConv
#This file stores the monitor that is used

class Monitor:
  def __init__(self, callback):
    self.state = "q2"
    self.output = None
    self.callback = callback

  
  
  def transit_to_q4(self):
    self.state = "q4"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q0(self):
    self.state = "q0"
    self.output = False
    self.callback(self.output)
  
  
  def transit_to_q3(self):
    self.state = "q3"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q1(self):
    self.state = "q1"
    self.output = None
    self.callback(self.output)
  
  
  def transit_to_q2(self):
    self.state = "q2"
    self.output = None
    self.callback(self.output)
  

  
  def transit(self, assignment):


    if self.state == "q4":
      if ((assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["dangerred"] and assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["dangerred"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["dangerred"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"])):
        self.transit_to_q0()
      if ((assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q3()
      if ((assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"])):
        self.transit_to_q1()
      if ((not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q4()
      return



    if self.state == "q0":
      self.transit_to_q0()
      return



    if self.state == "q3":
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"]) or (assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"])):
        self.transit_to_q1()
      if ((assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"])):
        self.transit_to_q3()
      if ((assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["pipes"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["dangerred"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["tankset"])):
        self.transit_to_q0()
      return



    if self.state == "q1":
      if ((assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["dangerred"] and assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q0()
      if ((assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["ipone"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["pipes"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["dangerred"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["t2bottom"]) or (not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"])):
        self.transit_to_q1()
      return



    if self.state == "q2":
      if (assignment["ipone"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q4()
      if ((assignment["ipone"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["pipes"]) or (assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"]) or (assignment["ipone"] and assignment["pipes"] and not assignment["dangerred"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["tankset"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["pipes"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"]) or (assignment["dangerred"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["dangerred"] and assignment["pipes"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["tankset"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["ipone"] and assignment["t2bottom"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["pipes"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["dangerred"] and assignment["t2bottom"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"]) or (assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"]) or (assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]) or (assignment["tankset"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"]) or (assignment["pipes"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["tankset"]) or (assignment["t2bottom"] and not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["tankset"])):
        self.transit_to_q0()
      if (assignment["ipone"] and assignment["t2bottom"] and not assignment["dangerred"] and not assignment["pipes"] and not assignment["tankset"]):
        self.transit_to_q3()
      if ((assignment["ipone"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"] and not assignment["pipes"]) or (assignment["ipone"] and assignment["pipes"] and assignment["t2bottom"] and assignment["tankset"] and not assignment["dangerred"])):
        self.transit_to_q1()
      if (not assignment["dangerred"] and not assignment["ipone"] and not assignment["pipes"] and not assignment["t2bottom"] and not assignment["tankset"]):
        self.transit_to_q2()
      return


