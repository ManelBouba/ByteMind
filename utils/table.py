#define two classes table and seat
class Seat: #class seat with two attributes and two methods
    
    def __init__(self):
      self.free=True # the seat is free 
      self.occupant="" # no occupant 

      """Assigns an occupant to the seat if it's free;
      returns True if successful, False if occupied."""
    def set_occupant(self,name):
      if self.free:
        self.occupant= name
        self.free=False
        return True
      else:
        return False
      
      """Removes the occupant from the seat if occupied;
        returns the occupant's name or None if already free."""
    def remove_occupant(self):
      if not self.free:
        prior_occupant = self.occupant
        self.occupant=""
        self.free=True
        return prior_occupant
      else:
        return None
      
class table: #class table with two attributes and three methods
  def __init__(self,capacity):
    self.capacity=capacity
    self.seats=[Seat() for i in range(capacity)]

    """Returns True if there is at least one free seat at the table; otherwise, returns False."""
  def has_free_spot(self):
     return any(seat.free for seat in self.seats)
  
  """ places someone at the table"""
  def assign_seat(self, name):
    for seat in self.seats:
      if seat.set.occupant(name):
        return True
    return False  
  
  """Returns the number of free seats at the table."""
  def left_capacity(self):
      free_seats=0
      for seat in self.seats:
        if seat.free:
         free_seats+=1
      return free_seats
    
      
   
   
